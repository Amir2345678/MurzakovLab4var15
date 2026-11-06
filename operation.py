import math
from constants import SHEAR_MODULUS_G
def calculate_torsion(T: float, d: float, L: float, tau_allow: float):
    T_mm = T * 1000.0
    tau = (16.0 * T_mm) / (math.pi * (d ** 3))
    phi_rad = (T_mm * L * 32.0) / (SHEAR_MODULUS_G * math.pi * (d ** 4))
    phi_deg = phi_rad * (180.0 / math.pi)
    utilization_ratio = tau / tau_allow
    if utilization_ratio < 0.5:
        status = "Большой запас"
    elif 0.5 <= utilization_ratio <= 1.0:
        status = "Допустимо"
    else:
        status = "Недопустимо"
    return {
        "tau": tau,
        "tau_allow": tau_allow,
        "phi_rad": phi_rad,
        "phi_deg": phi_deg,
        "ratio": utilization_ratio,
        "status": status
    }