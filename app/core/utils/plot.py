import matplotlib.pyplot as plt


def plot_points(x:list, y:list) :
    plt.savefig('./img/test.png')


def plot_line_and_points(x:list, y:list, m:float, c:float ):
    fi_y = m + c

    label_x = x.pop(0)
    label_y = y.pop(0)

    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(x, y)
    plt.scatter(x,y)
    plt.plot([0,1], [c, m + c], c ='r')
    plt.savefig('./img/line.png')

