# This contains helper functions for Labscripts
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# This function computes the actual position
def xpos(species):
    return (species.particles['ix'] + species.particles['x']) * species.dx
    

# This function creates 2D colormap plots of charge density and electric field over time
def plot_field_and_charge(sim, charge_data_time, E_data_time, tmax):
    fig, axs = plt.subplots(2, 1, figsize=(6, 4))
    xlims = [sim.dx/2,sim.box - sim.dx/2]
    tlims = [0,tmax]

    # Subfigure (a): Charge Density
    im0 = axs[0].imshow(charge_data_time, cmap="RdBu", interpolation='nearest',  aspect='auto',extent=[tlims[0],tlims[1],xlims[0],xlims[1]])
    axs[0].set_title('Charge Density')
    axs[0].set_xlabel(f"$\omega_pt$")
    axs[0].set_ylabel(f"$x\omega_p/c$")
    cbar0 = plt.colorbar(im0, ax=axs[0], fraction=0.046, pad=0.04)

    # Subfigure (b): Electric Field
    im1 = axs[1].imshow(E_data_time, cmap="RdBu", interpolation='nearest', aspect='auto',extent=[tlims[0],tlims[1],xlims[0],xlims[1]])
    axs[1].set_title('Electric Field')
    axs[1].set_xlabel(f"$\omega_pt$")
    axs[1].set_ylabel(f"$x\omega_p/c$")
    cbar1 = plt.colorbar(im1, ax=axs[1], fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()
    return  

# This function plots the phase space of a given species at the current simulation time
def plot_phase_space(sim,species,grid_size,xrange,vrange):
    plt.figure(figsize=(6, 4))
    #plt.plot(xpos(species),  species.particles['vx'],  'b.', ms=2,alpha=0.5, label = "Left")
    if not (isinstance(species,list) or isinstance(species,tuple)):
        img = np.flipud(np.abs(species.phasespace(['x1','v1'], grid_size, [xrange, vrange])))
        mycmap = cm.magma
        plt.imshow(img, cmap=mycmap, extent=(xrange[0],xrange[1],vrange[0],vrange[1]), aspect='auto', interpolation='none')
    else:  
        for ix, s in enumerate(species):
            img = np.flipud(np.abs(s.phasespace(['x1','v1'], grid_size, [xrange, vrange])))
            mycmap = cm.magma
            if ix>0:
                img = np.ma.masked_where(img < 1e-6*np.max(np.max(img)), img)
            plt.imshow(img, cmap=mycmap, extent=(xrange[0],xrange[1],vrange[0],vrange[1]), aspect='auto', interpolation='none')
        
    plt.xlabel(f"$x\omega_p/c$")
    plt.ylabel(f"$v_x/c$")
    plt.title("$v_x-x$ phasespace at $t = ${:g}".format(sim.t))
    plt.grid(True)
    plt.axis('tight')
    plt.show()
    return


