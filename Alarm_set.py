#!/usr/bin/env python
# coding: utf-8

# In[5]:


import datetime
import time
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    try:
        alarm_time = alarm_time_entry.get()
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

        current_time = datetime.datetime.now()
        current_hour, current_minute, _ = current_time.hour, current_time.minute, current_time.second

        alarm_time_datetime = current_time.replace(hour=alarm_hour, minute=alarm_minute, second=0)

        if current_time > alarm_time_datetime:
            alarm_time_datetime += datetime.timedelta(days=1)

        time_to_wait = (alarm_time_datetime - current_time).total_seconds()
        alarm_message = alarm_message_entry.get() or "Wake up!"

        if time_to_wait > 0:
            time.sleep(time_to_wait)
            messagebox.showinfo('Alarm', alarm_message)

    except Exception as e:
        messagebox.showerror('Error', str(e))

app = tk.Tk()
app.title('Alarm Clock')

frame = tk.Frame(app, padx=20, pady=20)
frame.pack()

alarm_time_label = tk.Label(frame, text='Alarm Time (HH:MM):')
alarm_time_label.grid(row=0, column=0, sticky='w')

alarm_time_entry = tk.Entry(frame)
alarm_time_entry.grid(row=0, column=1)

alarm_message_label = tk.Label(frame, text='Alarm Message:')
alarm_message_label.grid(row=1, column=0, sticky='w')

alarm_message_entry = tk.Entry(frame)
alarm_message_entry.grid(row=1, column=1)

set_alarm_button = tk.Button(frame, text='Set Alarm', command=set_alarm)
set_alarm_button.grid(row=2, column=0, columnspan=2)

app.mainloop()


# In[ ]:




