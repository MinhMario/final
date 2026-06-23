class Booking:
    def __init__(self,id,customer_name,room_number,room_price,nights,service_fee,discount):
        self._id=id
        self._customer_name=customer_name
        self._room_number=room_number
        self._room_price=room_price
        self._nights=nights
        self._service_fee=service_fee
        self._discount=discount
        self._total_rent=0
        self._rent_type=0
    def calculate_total_rent(self):
        self._total_rent=self._room_price * self._nights + self._service_fee-self._discount
    def classify_rent(self):
        if self._total_rent>7000000:
            self._rent_type='Tiết kiệm'
        elif self._total_rent>=3000000:
            self._rent_type='Cao cấp'
        elif self._total_rent>1000000:
            self._rent_type='Tiêu chuẩn'
        else:
            self._rent_type='Tiết kiệm'
class BookingManager:
    def __init__(self):
        self.bookings = [Booking(1,'Minh',30,35,2,20,10)]
        for p in self.bookings:
            p.calculate_total_rent()
            p.classify_rent()
    @staticmethod
    def check_float(num):
        try:
            num=float(num)
            if num<0:
                return None
            return num
        except ValueError:
            return None
    @staticmethod
    def check_nights(num):
        try:
            num=int(num)
            if num<=0 or num>365:
                return None
            return num
        except ValueError:
            return None
    def find_id(self,id):
        for p in self.bookings:
            if p._id==id:
                return p
        return None
    def show_all(self):
        if not self.bookings:
            print('Chưa có phòng nào được đặt')
            return
        for p in self.bookings:
            print(f"{p._id}-{p._customer_name}-{p._room_number}-{p._total_rent}")
            
    def add_booking(self):
        while True:
            id = input("Nhập mã đặt phòng: ").strip()
            if not id:
                print("Mã đặt phòng không được rỗng!")
                continue
            if self.find_id(id):
                print(f"Mã [{id}] đã tồn tại!")
                continue
            break
        if not id :
            print("Mã đặt phòng không được để trống")
            return
        customer_name=input('Nhập họ tên khách hàng').strip().title()
        if not customer_name:
            print("Tên khách hàng không được để trống")
            return
        room_number=input('Nhập số phòng').strip()
        if not room_number:
            print('Số phòng không được để trống')
            return
        room_price=float(input('Nhập giá phòng').strip())
        if not self.check_float(room_price):
           print('Giá phòng một đêm phải lớn hơn hoặc bằng 0') 
           return
        nights=int(input('Nhập số đêm thuê').strip())
        if not self.check_nights(nights):
            print('Số đêm thuê phải là số nguyên từ 1 đến 365')
            return
        service_fee=float(input('Nhập phụ phí dịch vụ').strip())
        if service_fee<0:
            print('Phụ phí dịch vụ phải lớn hơn hoặc bằng 0')
            return
        discount=float(input('Nhập giảm giá').strip())
        if discount<0:
            print('Giảm giá phải lớn hơn hoặc bằng 0')
            return
        p=Booking(id,customer_name,room_number,room_price,nights,service_fee,discount)
        p.calculate_total_rent()
        p.classify_rent()
        self.bookings.append(p)
        print('Thông báo: Thêm đặt phòng thành công!')
    def update_booking(self):
        id=input('Nhập mã phòng cần cập nhật').strip().upper()
        result=self.find_id(id)
        if not result:
            print('Không tìm thấy phòng cần cập nhật')
        else:
            room_price=input('Nhập giá phòng').strip()
        if not self.check_float(room_price):
           print('Giá phòng một đêm phải lớn hơn hoặc bằng 0') 
           return
        nights=input('Nhập số đêm thuê').strip()
        if not self.check_nights(nights):
            print('Số đêm thuê phải là số nguyên từ 1 đến 365')
            return
        service_fee=input('Nhập phụ phí dịch vụ').strip()
        if service_fee<0:
            print('Phụ phí dịch vụ phải lớn hơn hoặc bằng 0')
            return
        discount=input('Nhập giảm giá').strip()
        if discount<0:
            print('Giảm giá phải lớn hơn hoặc bằng 0')
            return
        result._room_price=room_price
        result._nights=nights
        result._service_fee=service_fee
        result._discount=discount
        result.calculate_total_rent()
        result.classify_rent()
    def delete_booking(self):
        id=input('Người dùng nhập phòng cần xoá').strip()
        result=self.find_id(id)
        if not self.find_id(id):
            print('Không tìm thấy phòng cần xoá')
            return
        confirm=input('Bạn có chắc muốn xoá phòng này không(y/n)').strip().upper()
        if confirm=='Y':
            self.bookings.remove(result)
        elif confirm =='N':
            print('Huỷ thao tác')
            return
        else:
            print('Lựa chọn không hợp lệ')
            return
manager=BookingManager()
while True:

    choice=input('Nhập lựa chọn của bạn').strip()
    if choice=='1':
        manager.show_all()
    elif choice=='2':
        manager.add_booking()
    elif choice=='3':
        manager.update_booking()
    elif choice=='4':
        manager.delete_booking()
    elif choice=='6':
        print('Kết thúc chương trình')
        break
    else:
        print('Lựa chọn không hợp lệ')
        
            
        
        
        
