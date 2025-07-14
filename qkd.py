from interface import Qubit, QuantumDevice


def prepare_classical_message(bit: bool, q: Qubit) -> None:
    # If classical bit is one, prepare a qubit in |0>
    if bit:
        q.x()


def target_measure(q: Qubit) -> bool:
    return q.measure()


def send_classical_bit(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prepare_classical_message(bit, q)
        result = target_measure(q)
        q.reset()
    assert result == bit
