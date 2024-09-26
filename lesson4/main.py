# Реалізуйте простий інтерфейс для складної системи аудіоплеєра.
# Вимоги:
# Система складається з багатьох класів: AudioDecoder, AudioPlayer, FileReader, Equalizer тощо.
# Створіть клас AudioFacade, який спрощує використання цих класів для відтворення аудіо файлу.
# Клієнтський код повинен мати можливість відтворити аудіо, використовуючи лише методи AudioFacade.
# Підказки:
# AudioFacade інкапсулює складність внутрішніх систем та надає простий інтерфейс.

class AudioDecoder:
    def decode(self, file):
        print("Decoding audio file {}".format(file))
        return "decoded_audio"


class AudioPlayer:
    def play(self, file):
        print("Playing audio file {}".format(file))
        return "played_audio"


class FileReader:
    def read(self, file_path):
        print("Reading file {}".format(file_path))
        return "raw_audio_data"


class Equalizer:
    def apply_equalizer(self, audio_data, settings):
        print("Applying equalization, settings {}".format(settings))
        return "equalized_{}".format(audio_data)


class AudioFacade:
    def __init__(self):
        self.file_reader = FileReader()
        self.decoder = AudioDecoder()
        self.player = AudioPlayer()
        self.equalizer = Equalizer()

    def play_audio(self, file_path, equalizer_settings=None):
        raw_audio_data = self.file_reader.read(file_path)
        decoded_audio = self.decoder.decode(raw_audio_data)
        if equalizer_settings:
            decoded_audio = self.equalizer.apply_equalizer(decoded_audio, equalizer_settings)
        self.player.play(decoded_audio)


if __name__ == "__main__":
    audio_facade = AudioFacade()
    audio_facade.play_audio("song.mp3")
    audio_facade.play_audio("song.mp3", equalizer_settings={"bass": "high"})