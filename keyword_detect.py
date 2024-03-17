
import pyautogui
import time
from PIL import Image
import pytesseract
from datetime import datetime

from parameta import program_duration, interval_seconds,keyword

class MovieKeywordDetector:
    def __init__(self,interval_seconds:int,duration_seconds:int,image_save_directory:str,keyword:str):
        self.interval_seconds = interval_seconds
        self.duration_seconds = duration_seconds 
        self.image_save_directory= image_save_directory
        self.keyword = keyword

    def find_keyword_in_image(self,image_path):
        """
        画像内に特定のキーワードが含まれているかを判断する関数。

        :param image_path: 画像のパス
        :param keyword: 検索するキーワード
        :return: キーワードが含まれている場合はTrue、そうでない場合はFalse
        """
        try:
            text = pytesseract.image_to_string(Image.open(image_path),lang="jpn")
            return self.keyword in text
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return False

    def run(self):
        """
        定期的にスクリーンショットを取得して保存する関数。

        :param interval: スクリーンショットを取得する間隔（秒）
        :param duration: スクリーンショット取得を続ける時間（秒）
        :param save_dir: スクリーンショットを保存するディレクトリ
        """
        end_time = time.time() + self.duration_seconds
        while time.time() < end_time:
            screenshot = pyautogui.screenshot()
            now = datetime.now()
            time_record_name = now.strftime("%m-%d_%H:%M:%S")
            filename = f"{self.image_save_directory}/screenshot_{time_record_name}.png"
            screenshot.save(filename)
            if self.find_keyword_in_image(image_path=filename):
                print(f"check_{filename}")
            
            time.sleep(self.interval_seconds)
        

if __name__ == '__main__':
    detector = MovieKeywordDetector(
        interval_seconds = interval_seconds,
        duration_seconds = program_duration,
        image_save_directory= "screenshot",
        keyword = keyword,
    )
    detector.run()