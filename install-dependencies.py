import platform
import subprocess
import os

def install_front() -> None:
    print("\nInstalando dependencias del Frontend...")
    try:
        subprocess.check_call("npm install", shell=True, cwd="Frontend")
        print("Frontend instalado correctamente.\n")
    except subprocess.CalledProcessError:
        print("Error instalando dependencias del frontend. Intenta hacerlo manualmente.")

def install_back() -> None:
    backend_dir = "Backend"
    venv_dir = os.path.join("venv")

    system = platform.system()
    python_exec = "python3" if system != "Windows" else "python"

    pip_path = (
        os.path.join("venv", "Scripts", "pip.exe") if system == "Windows"
        else os.path.join("venv", "bin", "pip")
    )

    try:
        if not os.path.exists(os.path.join(backend_dir, venv_dir)):
            print("No se encontró entorno virtual. Creando uno...")
            subprocess.check_call(f"{python_exec} -m venv venv", shell=True, cwd=backend_dir)
        else:
            print("Entorno virtual ya existente.")

        print("Instalando dependencias del Backend...")
        subprocess.check_call(f"./{pip_path} install -r requirements.txt", shell=True, cwd=backend_dir)
        print("Backend instalado correctamente.\n")
    except subprocess.CalledProcessError:
        print("Error instalando dependencias del backend. Intenta hacerlo manualmente.")

def main():
    system = platform.system()
    print(f"Sistema detectado: {system}")
    print("Iniciando instalación de dependencias...\n")

    install_front()
    install_back()

    print("Instalación completada exitosamente.")

if __name__ == "__main__":
    main()
