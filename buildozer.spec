[app]

title = Pink Task Manager
package.name = pinktaskmanager
package.domain = org.amina

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.main = task_manager.py

version = 0.1

requirements = python3,kivy

orientation = portrait

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 1
