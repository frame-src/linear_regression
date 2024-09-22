import matplotlib.pyplot as plt


def create_ticks_list(l : list) :
    min_l = min(l)
    max_l = max(l)
    step = (max_l - min_l) / 5
    values = [min_l + step * i for i in range(6)]
    return values


def plot_points(x:list, y:list, name:str) :
    label_x = x.pop(0)
    label_y = y.pop(0)
    plt.figure()
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.plot(x,y, ".")
    t_list = create_ticks_list(x)
    if len(x) > 3:
        plt.xticks(t_list)
    plt.savefig(f"./img/point_{name}_{label_y}.png")
    plt.close() 


def plot_line_and_points(x:list, y:list, m:float, c:float, name:str):
    fi_y = m + c
    label_x = x.pop(0)
    label_y = y.pop(0)

    plt.figure()
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.scatter(x, y)
    plt.scatter(x,y)
    plt.plot([0,1], [c, m + c], c ='r')
    plt.savefig(f"./img/{name}_{label_y}.png")
    plt.close() 


