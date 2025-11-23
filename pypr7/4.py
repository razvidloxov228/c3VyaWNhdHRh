from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Copyable(ABC):
    @abstractmethod
    def copy_document(self, document):
        pass


class Printer(Printable):
    def print_document(self, document):
        print(f"Друк документа: {document}")


class Scanner(Scannable):
    def scan_document(self):
        print("Сканування документа... Збережено у форматі PDF.")


class MultiFunctionDevice(Printable, Scannable, Copyable):
    def print_document(self, document):
        print(f"Друк документа: {document}")

    def scan_document(self):
        print("Сканування документа... Збережено у форматі PDF.")

    def copy_document(self, document):
        print(f"Копіювання документа: {document}")

printer = Printer()
scanner = Scanner()
mfd = MultiFunctionDevice()

printer.print_document("Звіт за листопад")
scanner.scan_document()
mfd.print_document("Контракт")
mfd.scan_document()
mfd.copy_document("Фото паспорта")
