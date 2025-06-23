'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

'''
RESOLUÇÃO:

Realizada a criação das classes Auth Service, TaskService, NotificationService, ReportService, ErrorHandler e HandlerTasks para separar as responsabilidades por cada função.

'''

class AuthService:
    def conect_api(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
class TaskService:
    def create_task(self) -> None:
        print("Tarefa crida com sucesso.")

    def update_task(self) -> None:
        print("Tarefa alterada com sucesso.")

    def remove_task(self) -> None:
        print("Tarefa removida com sucesso.")

class NotificationService:
    def send_notification(self) -> None:
        print("Notificação enviada com sucesso.")

class ReportService:
    def generate_report(self) -> None:
        print("Relatório criado.")
    
    def send_report(self) -> None:
        print("Relatório enviado.")
    
class ErrorHandler:
    def verify_conect(self, message: str) -> Exception:
        raise Exception(message)
    
class HandlerTasks:
    def __init__(self):
        self.authservice = AuthService()
        self.taskservice = TaskService()
        self.notification_service = NotificationService()
        self.report_service = ReportService()
        self.error_handler = ErrorHandler()

    def tasks_handlers(self, username: str, password: str) -> None:
        if self.authservice.conect_api(username, password):
            self.taskservice.create_task
            self.taskservice.update_task
            self.taskservice.remove_task
            self.notification_service.send_notification
            self.report_service.generate_report
            self.report_service.send_report
        else:
            raise Exception("Dados inválidos!")
            