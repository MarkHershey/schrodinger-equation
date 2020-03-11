import numpy as np
import scipy.constants as c

a = c.physical_constants['Bohr radius'][0]

def deg_to_rad(deg):
    return np.round(deg * c.pi / 180, 5)


def rad_to_deg(rad):
    return np.round(rad * 180 / c.pi, 5)


def spherical_to_cartesian(r,theta,phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.round(x, 5), np.round(y, 5), np.round(z, 5)


def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return np.round(r, 5), np.round(theta, 5), np.round(phi, 5)


def angular_wave_func(m, l, theta, phi):
    if l == 0:
        y = np.sqrt(1/(4*(np.pi)))
        return np.round(y, 5)
    elif l == 1:
        if m == 1:
            y = -(np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(phi*1j))
            return np.round(y, 5)
        elif m == 0:
            y = np.sqrt(3/(4*np.pi))*np.cos(theta)
            return np.round(y, 5)
        elif m == -1:
            y = np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(-phi*1j)
            return np.round(y, 5)
    elif l == 2:
        if m == 2:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(phi*2j)
            return np.round(y, 5)
        elif m == 1:
            y = -(np.sqrt(15/(32*np.pi))*np.cos(theta)*np.sin(theta)*np.exp(phi*1j))
            return np.round(y, 5)
        elif m == 0:
            y = np.sqrt(5/(16*np.pi))*(3*(np.cos(theta)**2)-1)
            return np.round(y, 5)
        elif m == -1:
            y = np.sqrt(15/(32*np.pi))*np.cos(theta)*np.sin(theta)*np.exp(-phi*1j)
            return np.round(y, 5)
        elif m == -2:
            y = np.sqrt(15/(32*np.pi))*(np.sin(theta)**2)*np.exp(-2j*phi)
            return np.round(y, 5)
    elif l == 3:
        if m == 3:
            y = -np.sqrt(35/(64*np.pi))*(np.sin(theta)**3)*np.exp(3j*phi)
            return np.round(y, 5)
        elif m == 2:
            y = np.sqrt(105/(32*np.pi))*np.cos(theta)*(np.sin(theta)**2)*np.exp(2j*phi)
            return np.round(y, 5)
        elif m == 1:
            y = -np.sqrt(21/(64*np.pi))*np.sin(theta)*(5*np.cos(theta)**2-1)*np.exp(phi*1j)
            return np.round(y, 5)
        elif m == 0:
            y = np.sqrt(7/(16*np.pi))*(5*(np.cos(theta)**3)-(3*np.cos(theta)))
            return np.round(y, 5)
        elif m == -1:
            y = np.sqrt(21/(64*np.pi))*np.sin(theta)*(5*np.cos(theta)**2-1)*np.exp(-1j*phi)
            return np.round(y, 5)
        elif m == -2:
            y = np.sqrt(105/(32*np.pi))*np.cos(theta)*(np.sin(theta)**2)*np.exp(-2j*phi)
            return np.round(y, 5)
        elif m == -3:
            y = np.sqrt(35/(64*np.pi))*(np.sin(theta)**3)*np.exp(-3j*phi)
            return np.round(y, 5)
    else:
        print("Not Supported")


def radial_wave_func(n,l,r):
    # common term
    common = np.exp(-r / (n * a))

    if n == 1:
        return np.round(2*common, 5)
    elif n == 2:
        if l == 0:
            return np.round((1/np.sqrt(2))*(1-(r/(2*a)))*common, 5)
        elif l == 1:
            return np.round((1/np.sqrt(24))*(r/a)*common, 5)

    elif n == 3:
        if l == 0:
            return np.round((2/(81*np.sqrt(3)))*(27-(18*r/a)+(2*(r/a)**2))*common, 5)

        elif l == 1:
            return np.round((8/(27*np.sqrt(6)))*(1-(r/(6*a)))*(r/a)*common, 5)

        elif l == 2:
            return np.round((4/(81*np.sqrt(30)))*((r/a)**2)*common, 5)

    elif n == 4:
        if l == 0:
            return np.round(1/4*(1-(0.75*(r/a))+(0.125*((r/a)**2))-((1/192)*((r/a)**3)))*common, 5)

        elif l == 1:
            return np.round(((np.sqrt(5))/(16*np.sqrt(3)))*(r/a)*(1-(0.25*(r/a))+((1/80)*((r/a)**2)))*common, 5)

        elif l == 2:
            return np.round((1/(64*np.sqrt(5)))*((r/a)**2)*(1-((r/a)/12))*common, 5)

        elif l == 3:
            return np.round((1/(768*np.sqrt(35)))*((r/a)**3)*common, 5)
    else:
        print("Not Supported")


def mgrid3d(xstart, xend, xpoints,
            ystart, yend, ypoints,
            zstart, zend, zpoints):
    xr = []
    yr = []
    zr = []
    xval = xstart
    xcount = 0

    # calculate the step size for each axis
    xstep = (xend - xstart) / (xpoints - 1)
    ystep = (yend - ystart) / (ypoints - 1)
    zstep = (zend - zstart) / (zpoints - 1)

    while xcount < xpoints:
        # initialize y points
        yval = ystart
        ycount = 0
        # create temporary variable to store x, y and z list
        xrow = []
        yrow = []
        zrow = []

        while ycount < ypoints:
            # initialize z points
            zval = zstart
            zcount = 0
            # create temporary variable to store the inner x, y, and z list
            xtmp = []
            ytmp = []
            ztmp = []

            while zcount < zpoints:
                # add the points x, y, and z to the inner most list
                xtmp.append(xval)
                ytmp.append(yval)
                ztmp.append(zval)

                # increase z point
                zval += zstep
                zcount += 1
            # add the inner most lists to the second lists
            xrow.append(xtmp)
            yrow.append(ytmp)
            zrow.append(ztmp)

            # increase y point
            yval += ystep
            ycount += 1
        # add the second lists to the returned lists
        xr.append(xrow)
        yr.append(yrow)
        zr.append(zrow)

        # increase x point
        xval += xstep
        xcount += 1

    return np.array([xr, yr, zr])


def hydrogen_wave_func(n,l,m,roa,Nx,Ny,Nz):

    # vectorizing functions
    v_cartesian_to_spherical = np.vectorize(cartesian_to_spherical)
    v_angular_wave_func = np.vectorize(angular_wave_func)
    v_radial_wave_func = np.vectorize(radial_wave_func)

    # generate 3d grid
    x, y, z = mgrid3d(-roa, roa, Nx,
                   -roa, roa, Ny,
                   -roa, roa, Nz)

    # convert to spherical coordinates
    r, theta, phi = v_cartesian_to_spherical(x, y, z)

    # to obtain the radial wave function
    # a = c.physical_constants['Bohr radius'][0]
    radial = v_radial_wave_func(n, l, r * a)

    # to obtain the real angular wave function
    if m < 0:
        angular = (1j/np.sqrt(2)) * (v_angular_wave_func(m,l,theta,phi) - (((-1)**m)*v_angular_wave_func(-m,l,theta,phi)))
    elif m == 0:
        angular = v_angular_wave_func(m, l, theta, phi)
    else: # m > 0
        angular = (1/np.sqrt(2)) * (v_angular_wave_func(-m,l,theta,phi) + (((-1)**m)*v_angular_wave_func(m,l,theta,phi)))

    # combined wave function
    wave = radial * angular

    # probability
    mag = np.power(np.real(wave), 2)

    # round everything
    x = np.round(x, 5)
    y = np.round(y, 5)
    z = np.round(z, 5)
    mag = np.round(mag, 5)

    return x,y,z,mag
