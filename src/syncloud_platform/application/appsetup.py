from syncloud_platform.systemd import systemctl

class AppSetup:

    def __init__(self, app_name, app_paths, nginx, storage, device_info, device):
        self.app_name = app_name
        self.app_paths = app_paths
        self.nginx = nginx
        self.storage = storage
        self.device_info = device_info
        self.device = device

    def get_install_dir(self):
        return self.app_paths.get_install_dir()

    def get_data_dir(self, remove_existing=False):
        return self.app_paths.get_data_dir(remove_existing)

    def register_web(self, port):
        self.nginx.add_app(self.app_name, port)

    def unregister_web(self):
        self.nginx.remove_app(self.app_name)

    def init_storage(self, user):
        return self.storage.init_app_storage(self.app_name, user)

    def device_domain_name(self):
        return self.device_info.domain()

    def app_domain_name(self):
        return self.device_info.app_domain(self.app_name)

    def app_url(self):
        return self.device_info.url(self.app_name)

    def add_port(self, local_port, protocol):
        self.device.add_port(local_port, protocol)

    def remove_port(self, local_port, protocol):
        self.device.remove_port(local_port, protocol)

    def add_service(self, service_name):
        systemctl.add_service(self.app_name, service_name)

    def remove_service(self, service_name):
        systemctl.remove_service(service_name)

    def restart_service(self, service_name):
        systemctl.restart_service(service_name)

    def reload_service(self, service_name):
        systemctl.reload_service(service_name)