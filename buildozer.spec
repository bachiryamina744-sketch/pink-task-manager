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
android.permissions = WRITE_EXTERNAL_STORAGE

# أضيفي هذه الأسطر في ملف buildozer.spec:
android.api = 33
android.min_api = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
