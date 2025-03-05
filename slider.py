def plot_slider(data_array):
    """
    Plot slider for DataArray.

    Args:
        data_array (da): DataArray with data
    """
    import xarray as xr
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider

    # Assuming data_array is your DataArray with dimensions (time, lat, lon)
    # Create a figure and axis
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    # Initial plot
    time_index = 0
    data = data_array.isel(time=time_index)
    im = ax.imshow(data, origin='lower', aspect='auto')
    plt.colorbar(im, ax=ax)

    # Slider axis
    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
    time_values = data_array['time'].values
    slider = Slider(ax_slider, 'Time', 0, len(time_values) - 1, valinit=0, valstep=1)

    # Update function
    def update(val):
        time_index = int(slider.val)
        data = data_array.isel(time=time_index)
        im.set_data(data)
        ax.set_title(f'Time: {time_values[time_index]}')
        fig.canvas.draw_idle()

    # Connect the update function to the slider
    slider.on_changed(update)
        
    # Set the slider labels to the actual time values
    slider.valtext.set_text(str(time_values[0]))

    def update_slider_label(val):
        time_index = int(slider.val)
        slider.valtext.set_text(str(time_values[time_index]))

    slider.on_changed(update_slider_label)

    plt.show()
