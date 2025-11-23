from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def deliver(self, order: str) -> None:
        pass


class FedEx(DeliveryService):
    def deliver(self, order: str) -> None:
        print(f"Delivering '{order}' via FedEx")


class UPS(DeliveryService):
    def deliver(self, order: str) -> None:
        print(f"Delivering '{order}' via UPS")


class NovaPoshta(DeliveryService):
    def deliver(self, order: str) -> None:
        print(f"Delivering '{order}' via Nova Poshta")


class OrderProcessor:
    def __init__(self, delivery_service: DeliveryService) -> None:
        self.delivery_service = delivery_service

    def process_order(self, order: str) -> None:
        print(f"Processing order: {order}")
        self.delivery_service.deliver(order)


if __name__ == "__main__":
    fedex_service = FedEx()
    ups_service = UPS()
    np_service = NovaPoshta()

    processor1 = OrderProcessor(fedex_service)
    processor1.process_order("Laptop")

    processor2 = OrderProcessor(ups_service)
    processor2.process_order("Smartphone")

    processor3 = OrderProcessor(np_service)
    processor3.process_order("Books")
