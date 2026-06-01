# khởi tạo dl ban đầu
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

# menu chính
while True:
    print("===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-7): ").strip()

    match choice:
        case "1":
            print('Xem chi tiết giỏ hàng')
            if len(saving_accounts) == 0:
                print('Danh sách hiện tại đang trống!')
                continue

            #duyệt danh sách
            for index, item in enumerate(saving_accounts, start=1):
                account_id = item['account_id']
                customer_name = item['customer_name']
                balance = item['balance']
                term_months = item['term_months']
                interest_rate = item['interest_rate']
                status = item['status']

                print(f"{index}. Mã sổ: {item['account_id']} | Khách hàng: {item['customer_name']} | "
                      f"Số tiền gửi: {item['balance']} | Kỳ hạn: {item['term_months']} tháng | "
                      f"Lại suất: {item['interest_rate']}%/năm | Trạng thái: {item['status']}")
                

        case '2':
            print('Mở sổ tiết kiệm mới')
            raw_id = input('Mời bạn nhập vào id sổ tiết kiệm mới: ').strip().upper()
            raw_name = input('Mời bạn nhập vào tên khách hàng: ').strip().title()
            raw_balance = input('Mời bạn nhập vào số tiên gửi: ').strip()
            raw_month = input('Mời bạn nhập vào kì hạn: ').strip()
            raw_rate = input('Mơi bạn nhập vào lãi suất: ').strip()

            # tên
            if len(raw_name) == 0:
                print('Tên của khách hàng không được để trống: ')
                continue
            
            # id
            check_id = False
            for item in saving_accounts:
                if item['account_id'] == raw_id:
                    print('Mã sổ tiết kiệm không được trùng')
                    check_id = True
                    continue
            
            # tiền nhập vào
            if not raw_balance.isdigit():
                print('Số tiền gửi phải nhập vào số nguyên dương hợp lệ')
                continue

            int_balance = int(raw_balance)
            
            if int_balance <= 0:
                print('Số lượng phải lớn hơn 0!')
                continue
            
            # tháng nhập vào
            if not raw_month.isdigit():
                print('Kỳ hạn gửi phải nhập vào số nguyên dương hợp lệ')
                continue

            int_month = int(raw_month)
            
            if int_month <= 0:
                print('Số lượng phải lớn hơn 0!')
                continue
            
            # lãi suất nhập vào
            if not raw_rate.isdigit():
                print('Lãi suất gửi phải nhập vào số nguyên dương hợp lệ')
                continue

            float_rate = float(raw_rate)
            
            if float_rate <= 0:
                print('Số lượng phải lớn hơn 0!')
                continue

            if not check_id:
                new_item = {
                    "account_id": raw_id,
                    "customer_name": raw_name,
                    "balance": raw_balance,
                    "term_months": raw_month,
                    "interest_rate": raw_rate,
                    "status": "active"
                } 
                saving_accounts.append(new_item)
                print('Đã thêm thành công sổ tiết kiệm mới!')
        
        case '3':
            print('Cập nhật thông tin sổ  tieets kiệm')
            raw_id = input('Mời bạn nhập vào id sổ cần cập nhật: ').strip().upper()

            # thấy
            target_account = None
            for item in saving_accounts:
                if item["account_id"] == raw_id:
                    target_account = item
                    break
            
            # k thấy
            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
            
            new_name = input("Nhập tên khách hàng mới: ").strip()
            raw_balance = input("Nhập số tiền gửi mới: ").strip()
            raw_month = input("Nhập kỳ hạn mới theo tháng: ").strip()
            raw_rate = input("Nhập lãi suất năm mới: ").strip()

            # tên
            if len(new_name) == 0:
                print("Tên khách hàng không được để trống")
                continue
            
            # tiền và tháng
            if not (raw_balance.isdigit() and raw_month.isdigit()):
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
            
            # nhập k hợp lệ
            int_balance = int(raw_balance)
            int_month = int(raw_month)
            if int_balance <= 0 or int_month <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
            
            # lãi suất
            if not raw_rate.isdigit():
                print("Lại suất không hợp lệ!")
                continue
            
            float_rate = float(raw_rate)
            if float_rate <= 0:
                print("Lại suất không hợp lệ!")
                continue
            
            # cập nhật
            target_account["customer_name"] = new_name
            target_account["balance"] = int_balance
            target_account["term_months"] = int_month
            target_account["interest_rate"] = float_rate
            print(f"Cập nhật thành công thông tin sổ tiết kiệm {raw_id}")

        case '4':
            print('Tất toán sổ tiết kiệm')
            raw_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

            target_account = None
            for item in saving_accounts:
                if item["account_id"] == raw_id:
                    target_account = item
                    break

            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            target_account["status"] = "closed"
            print(f"Tất toán thành công")

        case '5':
            print('Tính lãi dự kiến')
            
            raw_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            
            target_account = None
            for item in saving_accounts:
                if item["account_id"] == raw_id:
                    target_account = item
                    break
            
            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
                
            balance = target_account["balance"]
            rate = target_account["interest_rate"]
            months = target_account["term_months"]
            
            interest_earned = balance * rate / 100 * months / 12
            total_received = balance + interest_earned

            print(f"Tiền lãi dự kiến nhận được khi đến hạn: {interest_earned:,.1f} VNĐ")

        case '6':
            print('Kiểm tra điều kiện rút trước hạn')
            raw_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            raw_real_month = input("Nhập số tháng thực gửi: ").strip()
            
            if not raw_real_month.isdigit():
                print("Số tháng thực gửi không hợp lệ!")
                continue
                
            int_real_months = int(raw_real_month)

            if int_real_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            target_account = None
            for item in saving_accounts:
                if item["account_id"] == raw_id:
                    target_account = item
                    break
                    
            if target_account is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if target_account["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            balance = target_account["balance"]
            base_term = target_account["term_months"]

            if int_real_months < base_term:
                applied_rate = 0.5
                print(" Khách hàng rút TRƯỚC HẠN")
            else:
                applied_rate = target_account["interest_rate"]
                print(f"Khách hàng đủ điều kiện hưởng lãi ĐÚNG HẠN")
                
            interest_earned = balance * applied_rate / 100 * int_real_months / 12
            
            print(f"Tiền lãi thực nhận: {interest_earned:,.1f} VNĐ")

        case "7":
            print("Thoát hệ thống quản lý tài khoản TechBank!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")