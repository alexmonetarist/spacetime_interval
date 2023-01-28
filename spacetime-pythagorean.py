import numpy as np
import matplotlib.pyplot as plt


print("Detta program räknar ut rumtidsavståndet mellan två angivna punkter i rumtiden.")


def spacetime_interval(worldline):
    #Applies the spacetime interval formula; interval rounded to two decimals. 
    sides = np.array([np.abs(worldline[0][1] - worldline[0][0]), np.abs(worldline[1][1] - worldline[1][0])])
    return np.round(np.sqrt(np.amax(sides)**2 - np.amin(sides)**2), decimals=2)


def main():
    try:
        #User input of two points in spacetime
        x1 = float(input("Ange första händelsens rumskoordinat: "))
        t1 = float(input("Ange första händelsens tidskoordinat: "))
        x2 = float(input("Ange andra händelsens rumskoordinat: "))
        t2 = float(input("Ange andra händelsens tidskoordinat: "))
        
        worldline = np.array([[t1, t2], [x1, x2]]) #2D-matrix of the worldline

        k = (worldline[0][1] - worldline[0][0]) / (worldline[1][1] - worldline[1][0]) #Slope of the world line
        
        #Timelike, spacelike, or spacelike interval depending on the slope. 
        if k > 1:
            print(f"Rumtidsavståndet är tidslikt och {spacetime_interval(worldline)} sekunder.")

        elif k == 1:
            print(f"Rumtidsavståndet är ljuslikt och därmed {spacetime_interval(worldline)}.")

        else:
            print(f"Rumtidsavståndet är rumslikt och {spacetime_interval(worldline)} meter.")

        if input("Vill du visualisera rumtidsavståndet grafiskt? (J/N) \n").lower() != 'n':
            plt.ylabel("t (s)")
            plt.xlabel("x (m)")
            plt.plot(worldline[1], worldline[0])
            plt.show()

    except: 
        print("Endast reella koordinater är möjliga!")


if __name__=='__main__':
    while True:
        main()
        if input("Vill du räkna ut rumtidsavståndet för någon annan händelse? (J/N) \n").lower() != 'j':
            break