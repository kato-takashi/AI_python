#coding:UTF-8

#ニューロン
class Neuron:
    input_sum = 0.0

    def setinput(self, inp):
        self.input_sum += inp
        print(self.input_sum)

#ニューラルネットワーク
class NeuralNetwork:
    #ニューロンのインスタンス
    neuron = Neuron()
    #実行
    def commit(self, input_data):
        for data in input_data:
            self.neuron.setinput(data)

#ニューラルネットワークのインスタンス
neural_newwork = NeuralNetwork()

tral_data = [1.0, 2.0, 3.0]
neural_newwork.commit(tral_data)