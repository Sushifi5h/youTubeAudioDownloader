#depends on
import os
import shutil
import sys

class YouTubeDownloader:
	def __init__(self, cmdUrl):
		self.CONST_TEMPDIR = self.findCurrentDir() + "/tempYouTube"
		self.fileManagement()
		self.allUrl = []
		self.manageCmdUrls(cmdUrl)
		if(self.allUrl[0][-4::] != ".txt"):
			self.youtudeDownloader()
		else:
			self.fileExtractor()

	def manageCmdUrls(self, cmdUrl):
		for url in cmdUrl:
			if(url[-3::] != ".py"):
				self.allUrl.append(url)

	def logicForCmdUrls(self):
		for url in self.allUrl:
			self.youtudeDownloader(url)

	def findCurrentDir(self):
		curDir = os.path.dirname(os.path.realpath(__file__))
		return curDir

	def createTempDir(self):
		os.mkdir(self.CONST_TEMPDIR);

	def removeTempDir(self):
		shutil.rmtree(self.CONST_TEMPDIR)

	def youtudeDownloader(self):
		for url in self.allUrl:
			defaultCommand = "youtube-dl -i -x --audio-format mp3 --audio-quality 0 -o '" + self.CONST_TEMPDIR +"/%(title)s.%(ext)s' " + url
			os.system(defaultCommand)

	def singleDownload(self, url):
		defaultCommand = "youtube-dl -i -x --audio-format mp3 --audio-quality 0 -o '" + self.CONST_TEMPDIR +"/%(title)s.%(ext)s' " + url
		os.system(defaultCommand)

	def fileExtractor(self):
		songFile = open(self.findCurrentDir() + '/' + self.allUrl[0], 'r+')
		for line in songFile:
			self.singleDownload(line)

	def fileManagement(self):
		try:
			self.createTempDir()
			pass
		except OSError, e:
			self.removeTempDir()
			pass
		else:
			self.removeTempDir()
			pass
		finally:
			self.createTempDir()
			pass
		return 1


def main():
	if (len(sys.argv) >= 2):
		test = YouTubeDownloader(sys.argv)


if __name__ == '__main__':
	main()