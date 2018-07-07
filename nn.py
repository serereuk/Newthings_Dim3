import tensorflow as tf
import numpy as np
import os
from deep2 import deep2

class nn():
    def __init__(self, game):
        self.nnet = deep2(game)
        self.board_x , self.board_y = game.getboardsize()
        self.actionsize = game.actionsize()
        self.saver = None
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def train(self, examples):
        for epoch in range(100):
            print("epoch" + str(epoch + 1))
            batch_idx = 0
            while batch_idx < int(len(examples) / 50):
                sample_ids = np.random.randint(len(examples), size=50)
                boards, pis, vs = list(zip(*[examples[i] for i in sample_ids]))

                input_dict = {self.nnet.input_boards: boards, self.nnet.target_pis: pis, self.nnet.target_vs: vs,
                              self.nnet.dropout: 1.0, self.nnet.istraining: True}

                self.sess.run(self.nnet.train_step, feed_dict=input_dict)
                pi_loss, v_loss = self.sess.run([self.nnet.loss_pi, self.nnet.loss_v], feed_dict=input_dict)
                self.sess.run(self.nnet.total_loss)
                batch_idx += 1

    def predict(self, board):

        board = board[np.newaxis, :, :]

        prob, v = self.sess.run([self.nnet.prob, self.nnet.v],
                                feed_dict={self.nnet.input_boards: board, self.nnet.dropout: 0,
                                           self.nnet.istraining: False})

        return prob[0], v[0]

    def saving(self, folder, filename):
        filepath = os.path.join(folder, filename)
        if not os.path.exists(folder):
            os.mkdir(folder)

        if self.saver == None:
            self.saver = tf.train.Saver()

        self.saver.save(self.sess, filepath)

    def loading(self, folder, filename):
        filepath = os.path.join(folder, filename)
        self.saver = tf.train.Saver()
        self.saver.restore(self.sess, filepath)






