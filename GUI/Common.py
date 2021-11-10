def clear_master(master):
    slaves = master.grid_slaves()
    for slave in slaves:
        slave.destroy()
