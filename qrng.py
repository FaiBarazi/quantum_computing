from interface import QuantumDevice
from simulator import SingleQubitSimulator


def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()


if __name__ == "__main__":
    qsim = SingleQubitSimulator()
    for idx_sample in range(5):
        random_sample = qrng(qsim)
        print(f"QRNG returned {random_sample}.")
