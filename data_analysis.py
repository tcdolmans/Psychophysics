import pandas as pd
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
from statsmodels.stats.anova import AnovaRM
from scipy.stats import norm


def get_files_list():
    location = str(__file__)
    location = location[:-16]
    data_folder = location + "dataset/"
    files_list = listdir(data_folder)
    return data_folder, files_list


def clean_csv(data_folder, file):
    raw_data = pd.read_csv(data_folder + file)
    exp_data = pd.DataFrame(raw_data, columns=[
        "cue_stim_type",
        "cue_type",
        "expected_response",
        "key_resp.keys",
        "key_resp.rt",
        "key_resp_2.keys",
        "key_resp_2.rt"])
    exp_data = exp_data.drop([0, 81])
    return exp_data


def calc_acc(data_frame, condition):
    """Finds the number of correct/incorrect responses
    for each condition and type"""
    if condition == "endo":
        key_presses = "key_resp.keys"
    else:
        key_presses = "key_resp_2.keys"
    l_correct = data_frame[(data_frame.expected_response == "a") &
                           (data_frame[key_presses] == "a")]
    l_incorrect = data_frame[(data_frame.expected_response == "a") &
                             (data_frame[key_presses] == "l")]
    r_correct = data_frame[(data_frame.expected_response == "l") &
                           (data_frame[key_presses] == "l")]
    r_incorrect = data_frame[(data_frame.expected_response == "l") &
                             (data_frame[key_presses] == "a")]
    return len(l_correct), len(l_incorrect), len(r_correct), len(r_incorrect)


def calc_rt(data_frame):
    """Calculates mean RTs for each participant and condition"""
    endo_valid = data_frame[
        (data_frame.cue_stim_type == "endo") &
        (data_frame.cue_type == "correct") &
        (data_frame["key_resp.keys"] == data_frame.expected_response)]
    endo_valid = np.mean(endo_valid["key_resp.rt"])

    endo_invalid = data_frame[
        (data_frame.cue_stim_type == "endo") &
        (data_frame.cue_type == "incorrect") &
        (data_frame["key_resp.keys"] == data_frame.expected_response)]
    endo_invalid = np.mean(endo_invalid["key_resp.rt"])

    exo_valid = data_frame[
        (data_frame.cue_stim_type == "exo") &
        (data_frame.cue_type == "correct") &
        (data_frame["key_resp_2.keys"] == data_frame.expected_response)]
    exo_valid = np.mean(exo_valid["key_resp_2.rt"])

    exo_invalid = data_frame[
        (data_frame.cue_stim_type == "exo") &
        (data_frame.cue_type == "incorrect") &
        (data_frame["key_resp_2.keys"] == data_frame.expected_response)]
    exo_invalid = np.mean(exo_invalid["key_resp_2.rt"])
    return endo_valid, endo_invalid, exo_valid, exo_invalid


def plot_boxplot(en_v, en_i, ex_v, ex_i):
    fig, ax = plt.subplots()
    ax.boxplot([en_v, en_i, ex_v, ex_i])
    ax.set_ylabel("RT (s)")
    ax.set_xticklabels(
        ["Valid Endo",
         "Invalid Endo",
         "Valid Exo",
         "Ivalid Exo"])
    plt.show()


def do_anova(mean_rt):
    model = AnovaRM(data=mean_rt,
                    depvar="mean RT",
                    subject="participant",
                    within=["condition", "type"]).fit()
    return model


def calc_sdt(data_frame, condition):
    """Do calcs for d' and criterion per participant"""
    l_cor, l_incor, r_cor, r_incor = calc_acc(data_frame, condition)
    hit_rate = l_cor / (l_cor + l_incor + 1)
    fa_rate = (r_incor + 1) / (r_incor + r_cor + 1)

    d_prime = norm.ppf(hit_rate) - norm.ppf(fa_rate)
    criterion = -.5 * (norm.ppf(hit_rate) + norm.ppf(fa_rate))
    # print(hit_rate, fa_rate, criterion)
    return d_prime, criterion


if __name__ == "__main__":
    """Main loop that runs through the files and fucntions.
    Ugly, I know."""
    data_folder, files_list = get_files_list()
    endo_valid_rt, endo_invalid_rt, exo_valid_rt, exo_invalid_rt =\
        [], [], [], []

    mean_rt = pd.DataFrame(
        {"participant": [],
         "condition": [],
         "type": [],
         "mean RT": []})
    criteria = pd.DataFrame(
        {"participant": [],
         "valid_endo": [],
         "invalid_endo": [],
         "valid_exo": [],
         "invalid_exo": []})
    d_primes = pd.DataFrame(
        {"participant": [],
         "valid_endo": [],
         "invalid_endo": [],
         "valid_exo": [],
         "invalid_exo": []})

    for index, file in enumerate(files_list):
        exp_data = clean_csv(data_folder, file)
        endo_valid_df = exp_data[
            (exp_data.cue_type == "correct") &
            (exp_data.cue_stim_type == "endo")]
        endo_invalid_df = exp_data[
            (exp_data.cue_type == "incorrect") &
            (exp_data.cue_stim_type == "endo")]
        exo_valid_df = exp_data[
            (exp_data.cue_type == "correct") &
            (exp_data.cue_stim_type == "exo")]
        exo_invalid_df = exp_data[
            (exp_data.cue_type == "incorrect") &
            (exp_data.cue_stim_type == "exo")]

        d_prime_ven, criterion_ven = calc_sdt(endo_valid_df, "endo")
        d_prime_ien, criterion_ien = calc_sdt(endo_invalid_df, "endo")
        d_prime_vex, criterion_vex = calc_sdt(exo_valid_df, "exo")
        d_prime_iex, criterion_iex = calc_sdt(exo_invalid_df, "exo")

        appendingy = pd.DataFrame({"participant": [index + 1],
                                   "valid_endo": [d_prime_ven],
                                   "invalid_endo": [d_prime_ien],
                                   "valid_exo": [d_prime_vex],
                                   "invalid_exo": [d_prime_iex]})
        d_primes = d_primes.append(appendingy, ignore_index=True)

        appendingya = pd.DataFrame({"participant": [index + 1],
                                    "valid_endo": [criterion_ven],
                                    "invalid_endo": [criterion_ien],
                                    "valid_exo": [criterion_vex],
                                    "invalid_exo": [criterion_iex]})
        criteria = criteria.append(appendingya, ignore_index=True)

        aux_endo_val, aux_endo_inval, aux_exo_val, aux_exo_inval =\
            calc_rt(exp_data)
        endo_valid_rt.append(aux_endo_val)
        endo_invalid_rt.append(aux_endo_inval)
        exo_valid_rt.append(aux_exo_val)
        exo_invalid_rt.append(aux_exo_inval)

        p_num_list = [index, index, index, index]
        condition_list = ["endo", "endo", "exo", "exo"]
        type_list = ["valid", "invalid", "valid", "invalid"]
        mean_rt_list = [aux_endo_val, aux_endo_inval,
                        aux_exo_val, aux_exo_inval]
        new_lines = pd.DataFrame({"participant": p_num_list,
                                  "condition": condition_list,
                                  "type": type_list,
                                  "mean RT": mean_rt_list})

        mean_rt = mean_rt.append(new_lines, ignore_index=True)

    model = do_anova(mean_rt)
    print(model)
    plot_boxplot(endo_valid_rt, endo_invalid_rt, exo_valid_rt, exo_invalid_rt)
    print(np.mean(d_primes), np.mean(criteria))
