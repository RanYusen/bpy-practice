import bpy   # アドオン開発者に対して用意しているAPIを利用する

# アドオンに関する情報を保持する、bl_info変数
bl_info = {
    "name": "console_log_sample",
    "author": "YusenRan",
    "version": (0, 0),
    "blender": (3, 1, 2),
    "location": "Console",
    "description": "登録/解除時にログ出すだけのアドオン",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Development"
}

# アドオン有効化時の処理
def register():
    print("console_log_sampleが登録されました")


# アドオン無効化時の処理
def unregister():
    print("console_log_sampleが解除されました")


# メイン処理
if __name__ == "__main__":
    register()