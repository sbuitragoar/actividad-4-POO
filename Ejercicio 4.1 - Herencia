class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._num_consignaciones = 0  # Número de consignaciones realizadas
        self._num_retiros = 0  # Número de retiros realizados
        self._tasa_anual = tasa_anual  # Tasa anual de intereses
        self._comision_mensual = 0.0  # Comisión mensual de la cuenta

    def consignar(self, cantidad: float):
        if cantidad > 0:
            self._saldo += cantidad
            self._num_consignaciones += 1

    def retirar(self, cantidad: float):
        nuevo_saldo = self._saldo - cantidad
        if nuevo_saldo >= 0:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        tasa_mensual = self._tasa_anual / 12  # Convierte la tasa anual a mensual
        interes_mensual = self._saldo * tasa_mensual
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes()

class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000  # Activa si el saldo es mayor o igual a 10000

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)

    def extracto_mensual(self):
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()
        self._activa = self._saldo >= 10000

    def imprimir(self):
        print(f"Saldo = $ {self._saldo:.2f}")
        print(f"Comisión mensual = $ {self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._num_consignaciones + self._num_retiros}\n")

class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0.0  # Inicialmente no hay sobregiro

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._sobregiro > 0:
            residuo = self._sobregiro - cantidad
            if residuo > 0:
                self._sobregiro = residuo
            else:
                self._sobregiro = 0
                self._saldo = -residuo
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        print(f"Saldo = $ {self._saldo:.2f}")
        print(f"Comisión mensual = $ {self._comision_mensual:.2f}")
        print(f"Número de transacciones = {self._num_consignaciones + self._num_retiros}")
        print(f"Valor de sobregiro = $ {self._sobregiro:.2f}\n")

if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldo_inicial = round(float(input("Ingrese saldo inicial: $")), 2)
    tasa_interes = round(float(input("Ingrese tasa de interés: ")), 2)
    cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa_interes)

    cantidad_depositar = round(float(input("Ingresar cantidad a consignar: $")), 2)
    cuenta_ahorros.consignar(cantidad_depositar)

    cantidad_retirar = round(float(input("Ingresar cantidad a retirar: $")), 2)
    cuenta_ahorros.retirar(cantidad_retirar)

    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()
