def transformerstar(ra_e, dec_e, dist_e, ra_s, dec_s, dist_s):

    import numpy as np

    # Convert RA DEC Distance to Cartesian
    def curvecartesian(ra_deg, dec_deg, distance):
        ra_rad = np.radians(ra_deg)
        dec_rad = np.radians(dec_deg)
        
        x = distance * np.cos(dec_rad) * np.cos(ra_rad)
        y = distance * np.cos(dec_rad) * np.sin(ra_rad)
        z = distance * np.sin(dec_rad)
        
        return np.array([x, y, z])

    #Cartesian
    carte = curvecartesian(ra_e, dec_e, dist_e)
    carts = curvecartesian(ra_s, dec_s, dist_s)

    #B from A
    rely = carts - carte

    #Pancake
    x_prime = rely[0] / rely[2]
    y_prime = rely[1] / rely[2]
    return round(x_prime), round(y_prime) 

print(transformerstar(10, 10, 100, 20, 30, 500))