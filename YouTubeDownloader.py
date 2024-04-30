import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
import pytube
import os
import re
from ui.Design2 import Ui_MainWindow

class YoutubeDownloader(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Youtube Downloader')


        if getattr(sys, 'frozen', False):
            # Đang chạy từ tệp exe đã đóng gói
            image_path = os.path.join(sys._MEIPASS, "youtube.png")
        else:
            # Đang chạy từ mã nguồn .py
            image_path = "resource/youtube.png"
        
        self.label_4.setPixmap(QtGui.QPixmap(image_path))

        self.resolutionComboBox.addItem('144p')
        self.resolutionComboBox.addItem('240p')
        self.resolutionComboBox.addItem('360p')
        self.resolutionComboBox.addItem('480p')
        self.resolutionComboBox.addItem('720p')

        

        

        self.initSignal()

        self.statusbar.showMessage('Sẵn sàng.')
        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.statusbar.addPermanentWidget(self.progress_bar)

    # signal initialization
    def initSignal(self) :
        self.downloadButton.clicked.connect(self.downloadWork)
        self.toolButton.clicked.connect(self.savePathWork)
        
        

    # when the toolbox is clicked
    @pyqtSlot()
    def savePathWork(self) :
        fpath = QFileDialog.getExistingDirectory(self, 'Chọn đường dẫn')
        self.saveTextEdit.setText(fpath)

 

    @pyqtSlot()
    def downloadWork(self):
        # Step #1. Check url address
        url = self.urlTextEdit.text().strip()
        save = self.saveTextEdit.text()
        regex = re.compile(r'^https?://(?:www\.)?(?:youtube\.com/watch\?(?=.*v=\w+)|youtu\.be/[\w\-]+)$')

        if not url:
            QMessageBox.about(self, 'Lỗi', 'Chưa nhập URL của video')
            self.urlTextEdit.setFocus(True)
            return None

        if not save:
            QMessageBox.about(self, 'Lỗi', 'Chưa chọn đường dẫn')
            return None

        if not regex.match(url):
            QMessageBox.about(self, 'Lỗi', 'Sai định dạng URL Youtube')
            return None

        # Step #2. Download progress
        self.statusbar.showMessage('Đang tải xuống...')
        x = 5
        self.progress_bar.setValue(x)
        selected_resolution = self.resolutionComboBox.currentText()

        video = pytube.YouTube(url)
        stream = video.streams
        print(stream)
        selected_stream = None
        for s in stream:
            if s.resolution == selected_resolution and s.includes_audio_track:
                selected_stream = s
                break
        
        # Check if selected stream is None and resolution is 144p
        if selected_stream is None and selected_resolution == '144p':
            # Get the stream with itag 18 (assuming it corresponds to 144p)
            selected_stream = stream.get_by_itag(18)
        elif selected_stream is None and selected_resolution == '240p':
            # Get the stream with itag (adjust itag as needed)
            selected_stream = stream.get_by_itag(133)
        elif selected_stream is None and selected_resolution == '480p':
            # Get the stream with itag (adjust itag as needed)
            selected_stream = stream.get_by_itag(135)

        if selected_stream:
            self.progress_bar.setValue(60)
            down_dir = self.saveTextEdit.text()
            selected_stream.download(down_dir)
            self.statusbar.showMessage('Tải xuống thành công')
            self.progress_bar.setValue(100)
        else:
            QMessageBox.about(self, 'Lỗi', 'Không tìm thấy độ phân giải được chọn')
            self.statusbar.showMessage('Tải xuống thất bại')
            self.progress_bar.setValue(0)




     

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    you_viewer_main = YoutubeDownloader()
    you_viewer_main.show()
    app.exec_()
