class SensorECG:
    "Clase para la configuración de un módulo aplicado al área de Instrumentacion Biomedica."
    
    def __init__(self, modelo: str, ganancia: int, frecuencia_muestreo_hz: int):
        self.modelo = modelo
        self.ganancia = ganancia
        self.frecuencia_muestreo_hz = frecuencia_muestreo_hz

    def resumen_tecnico(self) -> str:
        "Devuelve un informe con las especificaciones del acondicionador de señal."
        return (
            f"=== Módulo de Bioelectrónica: {self.modelo} ===\n"
            f"• Ganancia del Amplificador: {self.ganancia}x\n"
            f"• Frecuencia de Muestreo: {self.frecuencia_muestreo_hz} Hz\n"
            f"• Estado: Circuito analógico listo para adquisición de biopotenciales."
        )
