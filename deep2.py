
import tensorflow as tf


class deep2():
    def __init__(self, game):
        self.board_x, self.board_y = game.getboardsize()
        self.actionsize = game.actionsize()

        relu = tf.nn.relu
        tanh = tf.nn.tanh
        batchnormalization = tf.layers.batch_normalization
        dropout = tf.layers.dropout
        dense = tf.layers.dense

        self.input_boards = tf.placeholder("float", shape=[None, self.board_x, self.board_y])
        self.dropout = tf.placeholder("float")
        self.istraining = tf.placeholder(tf.bool, name="is_training")


        x_image = tf.reshape(self.input_boards, [-1, self.board_x, self.board_y, 1])

        h_conv1 = relu(batchnormalization(self.conv2d(x_image, 64, "same"), axis=3, training=self.istraining))
        h_conv2 = relu(batchnormalization(self.conv2d(h_conv1, 128, "same"), axis=3, training=self.istraining))
        h_conv3 = relu(batchnormalization(self.conv2d(h_conv2, 256, "same"), axis=3, training=self.istraining))
        h_conv4 = relu(batchnormalization(self.conv2d(h_conv3, 512, "same"), axis=3, training=self.istraining))


        #h_conv5 = relu(batchnormalization(self.conv2d(h_conv4, 512, "same"), axis=3, training=self.istraining))
        #h_conv3 = relu(batchnormalization(self.conv2d(h_conv2, 512, "valid"), axis=3, training=self.istraining))
        #h_conv4 = relu(batchnormalization(self.conv2d(h_conv3, 512, "valid"), axis=3, training=self.istraining))

        h_conv4_flat = tf.reshape(h_conv4, [-1, 512 * (self.board_x) * (self.board_y)])
        s_fc1 = dropout(relu(batchnormalization(dense(h_conv4_flat, 1024), axis=1, training=self.istraining)), rate=1.0)
        s_fc2 = dropout(relu(batchnormalization(dense(s_fc1, 512), axis=1, training=self.istraining)), rate=1.0)
        self.pi = dense(s_fc2, self.actionsize)
        self.prob = tf.nn.softmax(self.pi)
        self.v = tanh(dense(s_fc2, 1))

        self.caculate_loss()

    def conv2d(self, x, out_channels, padding):
        return tf.layers.conv2d(x, out_channels, kernel_size=[3, 3], padding=padding)

    def caculate_loss(self):
        self.target_pis = tf.placeholder("float", shape=[None, self.actionsize])
        self.target_vs = tf.placeholder("float", shape=[None])
        self.loss_pi = tf.losses.softmax_cross_entropy(self.target_pis, self.pi)
        self.loss_v = tf.losses.mean_squared_error(self.target_vs, tf.reshape(self.v, shape=[-1, ]))
        self.total_loss = self.loss_pi + self.loss_v
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            self.train_step = tf.train.AdamOptimizer(0.001).minimize(self.total_loss)


# gbsize = 7; win_standard = 5
