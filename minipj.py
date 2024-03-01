from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg

sg.theme('DarkGrey3')
def show_graph(queue):
    names = [item['name'] for item in queue]
    count_seconds = [item['count_second'] for item in queue]
    fig, ax = plt.subplots()
    ax.bar(names, count_seconds)
    ax.set_xlabel('Customer_Name')
    ax.set_ylabel('Time (second)')
    ax.set_title('Graph Queue')
    plt.show()
class QueueManager:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    def get_queue(self):
        return self.queue




def main():
    # กำหนดรูปภาพที่จะแสดง
    image_path = 'D:/miniproject/img1.png'
    imgcone = 'D:/miniproject/cone.png'
    imgcup = 'D:/miniproject/cup.png'
    imggreentea = 'D:/miniproject/greentea.png'
    imgchocolatechip = 'D:/miniproject/chocolatechip.png'
    imgchocolate = 'D:/miniproject/chocolate.png'
    imgstawberry = 'D:/miniproject/stawberry.png'
    imgbread = 'D:/miniproject/bread.png'
    imgrainbow = 'D:/miniproject/rainbow.png'
    imgtoppingconflag = 'D:/miniproject/toppingconflag.png'
    imgtoppingrainbow = 'D:/miniproject/toppingrainbow.png'
    imgtoppingnuts = 'D:/miniproject/toppingnuts.png'
    imgtoppingchocolate = 'D:/miniproject/toppingchocolate.png'

    item_queue = QueueManager()

    # สร้างโครงสร้างหน้าต่าง GUI
    layout = [
        [sg.Text('ร้านไอติมซิ่ง', size=(30, 1), font=('Helvetica', 20), justification='center')],
        [sg.Frame(layout=[
            [sg.Button('ระบบขาย', size=(55, 2),key='selectitem')],
            [sg.Button('คิว', size=(55, 2),key='queue')],
            [sg.Button('กราฟ', size=(55, 2),key='graph')],
            [sg.Button('exit', size=(55, 2))]
        ], title='', title_color='blue', relief=sg.RELIEF_SUNKEN, font=('Helvetica', 12))],
        [sg.Image(filename=image_path, size=(495, 400), key='-IMAGE-')]
    ]

    # สร้างหน้าต่าง
    window = sg.Window('ร้านไอติมซิ่ง', layout, resizable=True, finalize=True, size=(500, 750))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        selected_item = []

        if event == 'selectitem':
            layout_popup = [
                [
                    sg.Text('ร้านไอติมซิ่ง', size=(30, 1), font=('Helvetica', 20), justification='center')
                 ],
                [
                    sg.Text('กรอกชื่อลูกค้า:', size=(20, 1), font=('Helvetica', 15), justification='left'),
                    sg.Text('ราคา:', size=(20, 1), font=('Helvetica', 15), justification='left'),
                 ],
                [
                    sg.InputText(size=(20, 1), font=('Helvetica', 15), key='-CUSTOMER_NAME-'),
                    sg.InputText(size=(20, 1), font=('Helvetica', 15), key='-Price-'),
                    sg.Button('save', size=(8, 2), font=('Helvetica', 15)),
                 ],
                [sg.Text('รายการที่เลือก:', size=(20, 1), font=('Helvetica', 15), justification='left'),
                sg.Text('', size=(20, 8), font=('Helvetica', 15), key='list_product', text_color='green',),
                 sg.Text('ข้อกำหนด\n'
                         '-เลือกถ้วยได้ 1 อย่าง\n'
                         '-เลือกไอติมได้ 3 ก้อน\n'
                         '-เลือกท็อปปิ้งได้ 4อย่าง\n'
                         'ทุกอย่าง 10 บาท', size=(20, 8), font=('Helvetica', 15), key='list_product', text_color='red', )
                 ],
                [sg.Frame(layout=[
                    [sg.Text('เลือกว่าใส่อะไร', size=(15, 1), font=('Helvetica', 15), justification='left')],
                    [sg.Button('ขนมปัง ',key="bread", size=(8, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgbread, size=(150, 150)),
                     sg.Button('ถ้วย',key="cup", size=(8, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgcup, size=(150, 150)),
                     sg.Button('โคน',key="cone", size=(8, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgcone, size=(150, 150))]
                ], title='', title_color='blue', relief=sg.RELIEF_SUNKEN, font=('Helvetica', 8))],
                [   sg.Frame(layout=[
                    [sg.Text('เลือกรสไอติม', size=(15, 1), font=('Helvetica', 15), justification='left')],
                    [sg.Button('สตอเบอรี่',key="Strawberry", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgstawberry, size=(150, 150)),
                     sg.Button('ช็อกโกแลต',key="Chocolate", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgchocolate, size=(150, 150)),
                     sg.Button('ช็อกโกแลตชิพ',key="ChocolateChips", size=(15, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgchocolatechip, size=(150, 150)),
                     sg.Button('ชาเขียว',key="Greentea", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imggreentea, size=(150, 150)),
                     sg.Button('เรนโบว์',key="Rainbow", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgrainbow, size=(150, 150))]
                ], title='', title_color='blue', relief=sg.RELIEF_SUNKEN, font=('Helvetica', 8))],
                [   sg.Frame(layout=[
                    [sg.Text('เลือกท็อปปิ้ง', size=(10, 1), font=('Helvetica', 15), justification='left')],
                    [sg.Button('คอนเฟล็ก',key="toppingconflag", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgtoppingconflag, size=(150, 150)),
                     sg.Button('เรนโบว์ไรซ์',key="toppingrainbow", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgtoppingrainbow, size=(150, 150)),
                     sg.Button('ถั่ว',key="toppingnuts", size=(10, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgtoppingnuts, size=(150, 150)),
                     sg.Button('ช็อกโกแลตไรซ์',key="toppingchocolate", size=(15, 2), font=('Helvetica', 8)),
                     sg.Image(filename=imgtoppingchocolate, size=(150, 150))

                     ]
                ], title='', title_color='blue', relief=sg.RELIEF_SUNKEN, font=('Helvetica', 8)),sg.Button('ยกเลิก', size=(15, 2), font=('Helvetica', 15),button_color=('white', 'red'))],

            ]

            window_popup = sg.Window('เลือกท็อปปิ้ง', layout_popup, resizable=True, finalize=True, size=(1300, 950))
            selected_item_counts = {'bcc': 0, 'icream': 0, 'tp': 0}
            count_second = 0
            item_price = 0
            while True:
                event_popup, values_popup = window_popup.read()

                if event_popup == sg.WINDOW_CLOSED:
                    break
                elif event_popup == 'ยกเลิก':
                    break
                elif event_popup in ['bread', 'cup', 'cone']:
                    if selected_item_counts['bcc'] < 1:
                        selected_item_counts['bcc'] += 1
                        selected_item.append(event_popup)
                        window_popup['list_product'].update('\n'.join(selected_item))
                        item_price += 10  # เพิ่มราคาทีละ 10
                        count_second += 10
                        window_popup['-Price-'].update(item_price)
                    else:
                        sg.popup("คุณเลือกเกิน")
                elif event_popup in ['Strawberry', 'Chocolate', 'ChocolateChips', 'Greentea', 'Rainbow']:
                    if selected_item_counts['icream'] < 3:
                        selected_item_counts['icream'] += 1
                        selected_item.append(event_popup)
                        window_popup['list_product'].update('\n'.join(selected_item))
                        item_price += 10  # เพิ่มราคาทีละ 10
                        count_second += 10
                        window_popup['-Price-'].update(item_price)
                    else:
                        sg.popup("คุณเลือกเกิน")
                elif event_popup in ['toppingconflag', 'toppingrainbow', 'toppingnuts', 'toppingchocolate']:
                    if selected_item_counts['tp'] < 4:
                        selected_item_counts['tp'] += 1
                        selected_item.append(event_popup)
                        window_popup['list_product'].update('\n'.join(selected_item))
                        item_price += 10  # เพิ่มราคาทีละ 10
                        count_second += 10
                        window_popup['-Price-'].update(item_price)
                    else:
                        sg.popup("คุณเลือกเกิน")




                elif event_popup == 'save':
                    item_name = values_popup['-CUSTOMER_NAME-']
                    item_price = values_popup['-Price-']
                    #item_second = values_popup['count+วิ']
                    item_queue.enqueue({'name': item_name, 'price': item_price,'count_second':count_second})
                    sg.popup(f"ชื่อลูกค้า: {item_name}     ราคา: {item_price} บาท")
                    selected_item = []  # เคลียร์รายการที่ถูกเลือก
                    window_popup['list_product'].update('')
                    window_popup.close()

            window_popup.close()


        elif event == 'queue':
            queue_layout = [
                [sg.Text('Item Queue', size=(30, 1), font=('Helvetica', 20), justification='center')],
                [sg.Listbox(values=[f" ชื่อ {item['name']}   ราคา {item['price']} บาท           เวลาโดยประมาณ {item['count_second']} วินาที"
                for item in item_queue.get_queue()],
                            size=(70, 10), font=('Helvetica', 15), key='-QUEUE-LIST-', enable_events=True)],
                [sg.Button('Clear Queue', size=(15, 2))]
            ]
            queue_window = sg.Window('Item Queue', queue_layout, resizable=True, finalize=True, size=(800, 500))
            while True:
                queue_event, _ = queue_window.read()
                if queue_event == sg.WINDOW_CLOSED:
                    break
                elif queue_event == 'Clear Queue':
                    if item_queue.get_queue():
                        item_queue.dequeue()
                        queue_window['-QUEUE-LIST-'].update(
                            values=[f" ชื่อ {item['name']}   ราคา {item['price']} บาท           เวลาโดยประมาณ {item['count_second']} วินาที"
                                    for item in item_queue.get_queue()])

        elif event == 'graph':
            show_graph(item_queue.get_queue())


        elif event == 'exit':
            confirm_exit = sg.popup_yes_no('คุณแน่ใจหรือไม่ว่าต้องการออกจากระบบ? ถ้าหากออกจากระบบแล้วจะไม่สามารถกู้คืนข้อมูลได้', title='ยืนยันการออกจากระบบ')
            if confirm_exit == 'Yes':
                break

    window.close()


if __name__ == '__main__':
    main()