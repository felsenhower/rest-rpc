import json

import matplotlib.pyplot as plt


def main() -> None:
    with open("runtimes.json", "r") as f:
        data = json.load(f)
    bars = plt.bar(data.keys(), data.values())
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
        )
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime: 1000x ApiClient accessor call")
    plt.savefig("benchmark.png")


if __name__ == "__main__":
    main()
