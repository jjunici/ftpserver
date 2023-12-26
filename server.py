from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
class MyHandler(FTPHandler):
    def on_login(self, username):
        # 사용자가 로그인할 때 호출되는 메서드
        print("접속 유저:" + username)
        if username == "test" and self.password == "1234":
            return "test"  # 인증 성공
        else:
            return "None"  # 인증 실패
    def on_logout(self, username):
        # 사용자가 로그 오프 할떄 호출되는 메서드 
        print("로그아웃 유저:",username)
        return super().on_logout(username)
def create_ftp_server():
  # 인증 설정
    authorizer = DummyAuthorizer()
    
    # 유저별 폴더 경로 설정 
    home_dir = os.path.join(os.getcwd(),'ftpstore')

    
    # 사용자 추가
    authorizer.add_user("test", "1234",home_dir, perm="elradfmw")

    # 핸들러 설정
    handler = MyHandler
    handler.authorizer = authorizer
    handler.banner = "Test FTP"
    
    # 서버 설정 및 시작 (모든 IP를 허용)
    server = FTPServer(("0.0.0.0", 21), handler)
    print("FTP 서버가 0.0.0.0:21에서 실행 중입니다.")
    server.serve_forever()

if __name__ == "__main__":
    create_ftp_server()
