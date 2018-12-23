# https://github.com/enkore/i3pystatus/

# PIP3 requirements:
# - colour (many modules)
# - netifaces (network)
# - xkbgroup (keyboard layout switching)
# - git+https://github.com/bastienleonard/pysensors  (not to be confused with pip-pysensors - required by temp)
# - psutil (required by mem)

# Mandatory
from i3pystatus import Status

# Ze log
status = Status(logfile='$HOME/.config/i3/i3pystatus.log')

# Clock
status.register("clock",
    format=" ⏰ %c",
    on_leftclick="gnome-calendar")

# CPU load
status.register("load",
    format=" 💥 {avg1} {avg5} {avg15} ",)

# CPU temps
status.register("temp",
    format=" 🔥 {Package_id_0}℃ |{Core_0_bar}|{Core_1_bar}|{Core_2_bar}|{Core_3_bar}| ",
    hints={"markup": "pango"},
    lm_sensors_enabled=True,
    dynamic_color=True)

# CPU usage bar
status.register("cpu_usage_bar",
    format=" {usage_bar_cpu0}|{usage_bar_cpu1}|{usage_bar_cpu2}|{usage_bar_cpu3}|{usage_bar_cpu4}|{usage_bar_cpu5}|{usage_bar_cpu6}|{usage_bar_cpu7}| ",
    bar_type="vertical")



# CPU graph
status.register("cpu_usage_graph",
    format=" {cpu_graph} ",
    graph_width=15)
# CPU frequency
status.register("cpu_freq",
    format=" 🏁 {avgg} ")

# Memory bar
# status.register("mem_bar",
#     format=" M: {used_mem_bar} ",
#     multi_colors=True)

# Memory numbers
status.register("mem",
    # format=" 📜 {used_mem}/{total_mem} ",
    format=" 📜 {used_mem} M ",
    round_size=None,)
    # divisor=1073741824)

# Network stats
status.register("network",
    interface="eno1",
    format_up=" 🌍 {interface} - {bytes_sent} Mbps - {bytes_recv} Mbps ",
    format_down=" {interface} - 🛑 ",
    sent_limit=24,
    recv_limit=240,
    divisor=125000,
    separate_color=True)

# RootFS usage
status.register("disk",
    path="/",
    format=" 💾: {used}/{total} ",
    round_size=None,
    critical_limit= 10 )

# Pulse audio volume
# How to get sink names:
# pacmd list-sinks | grep -e 'name:'
status.register("pulseaudio",
    format=" 🔊 {volume} ",
    step=1,
    sink="alsa_output.pci-0000_00_1b.0.iec958-stereo",)


# Language bar - should be at the end because of variable size.
status.register("xkblayout",
    format=" {symbol}{variant} ",
    layouts=["us","rs","rs(latin)"],
    on_leftclick=["change_layout",1],
    on_rightclick=["change_layout",-1] )

# Off to the races
status.run()
