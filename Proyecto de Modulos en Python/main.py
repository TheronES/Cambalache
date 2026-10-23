from modelos import SensorECG

def ejecutar_sistema():
    # llamacion del módulo de electrocardiografía con parámetros reales
    ecg_ad8232 = SensorECG(
        modelo="AD8232 (Biomedical ECG Front-End)",
        ganancia=1000,
        frecuencia_muestreo_hz=500
    )
    
    # Despliegue en consola del estado y especificaciones del sensor
    print(ecg_ad8232.resumen_tecnico())

if __name__ == "__main__":
    ejecutar_sistema()
