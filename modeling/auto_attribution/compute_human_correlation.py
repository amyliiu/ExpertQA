"""
Compute AutoAIS labels with respect to human judgements.
"""
from data_utils.jsonl_utils import read_jsonl
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def human_corr(autoais_test_file):
    examples = read_jsonl(autoais_test_file)

    preds = []
    golds = []

    per_sys_preds = {}
    per_sys_golds = {}
    for ex in examples:
        for system, answer in ex["answers"].items():
            if system not in per_sys_preds:
                per_sys_preds[system] = []
                per_sys_golds[system] = []

            for c in answer["claims"]:
                # If a claim is not worthy of citation, we skip it in the evaluation
                if c["worthiness"] == "No":
                    continue

                autoais_label = 1 if c["autoais_label"] == "Y" else 0
                gold_label = 1 if c["support"] == "Complete" else 0

                preds.append(autoais_label)
                golds.append(gold_label)
                per_sys_preds[system].append(autoais_label)
                per_sys_golds[system].append(gold_label)

    p, r, f1, sup = precision_recall_fscore_support(golds, preds, pos_label=1)

    print(f"Accuracy: {accuracy_score(golds, preds)}")
    print(f"Precision: {p}")
    print(f"Recall: {r}")
    print(f"F1: {f1}")
    print(f"Num Labels: {sup}")
    print(f"Num positives in gold = {sum(golds)} / {len(golds)}")

    for system, sys_golds in per_sys_golds.items():
        sys_preds = per_sys_preds[system]
        p, r, f1, sup = precision_recall_fscore_support(sys_golds, sys_preds, pos_label=1)

        print(f"\t{system}")
        print(f"\tAccuracy: {accuracy_score(sys_golds, sys_preds)}")
        print(f"\tPrecision: {p}")
        print(f"\tRecall: {r}")
        print(f"\tF1: {f1}")
        print(f"\tNum Labels: {sup}")
        print(f"\tNum positives in gold = {sum(sys_golds)} / {len(sys_preds)}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--autoais_test_set",
                        default="modeling/auto_attribution/domain_test_autoais_ft.jsonl",
                        help="example file with per-claim autoais labels",
                        type=str)
    args = parser.parse_args()

    human_corr(args.autoais_test_set)
