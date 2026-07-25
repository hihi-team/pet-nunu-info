<div align="center">

# 🐾 Petnunu

**Thú cưng ảo sống trên desktop của bạn — macOS · Windows · Linux.**

Pet đi lại, nhảy, leo mép màn hình và ngủ trong một cửa sổ trong suốt nổi trên mọi app —
điều khiển từ khay hệ thống, kèm Pomodoro & focus mode để bạn làm việc vui hơn.

[![Download](https://img.shields.io/github/v/release/hihi-team/pet-nunu-info?label=Download&style=for-the-badge&color=ff8fab)](https://github.com/hihi-team/pet-nunu-info/releases/latest)
&nbsp;
![macOS](https://img.shields.io/badge/macOS-14%2B-black?style=for-the-badge&logo=apple)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=for-the-badge&logo=windows)
![Linux](https://img.shields.io/badge/Linux-X11-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## ⬇️ Tải về

Tải bản mới nhất ở **[Releases](https://github.com/hihi-team/pet-nunu-info/releases/latest)** rồi chọn file theo hệ điều hành:

| Hệ điều hành | File tải | Cài đặt |
|---|---|---|
| 🍎 **macOS** 14+ | `Petnunu-macOS-*.dmg` (hoặc `.zip`) | Mở `.dmg` → kéo **Petnunu.app** vào **Applications** |
| 🪟 **Windows** 10/11 | `Petnunu_*-setup.exe` (hoặc `.msi`) | Chạy file cài đặt → next → xong |
| 🐧 **Linux** (X11) | `Petnunu_*.AppImage` · `.deb` | AppImage: `chmod +x` rồi chạy · `.deb`: `sudo dpkg -i` |

### Ghi chú lần đầu mở
- **macOS** — app phân phối ngoài App Store: **chuột phải → Open → Open**. Nếu báo *"is damaged"*:
  ```bash
  xattr -dr com.apple.quarantine /Applications/Petnunu.app
  ```
- **Windows** — SmartScreen có thể hiện *"Windows protected your PC"* → **More info → Run anyway** (app chưa mua chứng chỉ ký số).
- **Linux** — hỗ trợ tốt nhất trên **X11**. Trên **GNOME Wayland**, hãy đăng nhập phiên **"Xorg/X11"** để pet định vị & luôn-nổi-trên-cùng hoạt động đúng.

**Yêu cầu:** macOS 14 (Sonoma)+ · Windows 10/11 · Linux desktop chạy X11/XWayland.

---

## ✨ Tính năng

- 🐣 **Pet overlay** — đi/nhảy/ngủ, leo & bám mép màn hình, nhìn/đi theo con trỏ, kéo thả tự do.
- 💖 **Chăm sóc & cảm xúc** — cho ăn, vuốt ve, chơi, ru ngủ; chỉ số happiness / energy / hunger / affection.
- 🪙 **Coin, nhiệm vụ & thành tựu** — daily mission, achievement, ví coin.
- 🍅 **Pomodoro & Focus mode** — nhắc nghỉ / uống nước / nghỉ mắt, thống kê focus (ngày/tuần, streak).
- 🛒 **Pet Store** — mua thêm pet bằng coin.
- 🌱 **Nuôi pet lên level** + bảng xếp hạng cộng đồng.
- 🎨 **Petnunu Studio** — tự tạo pet.
- 📦 **Import pet pack** của riêng bạn.
- 🖥️ **Multi-monitor**, khay hệ thống (tray/menu bar), onboarding, âm thanh.

> Tài khoản, ví coin, cửa hàng và pet pack **dùng chung** giữa cả ba nền tảng.

---

## 🌐 Liên kết

- 🏠 Cộng đồng **Petnunu World** — kho pet, forum, leaderboard *(web)*
- 📝 **[Changelog / What's new](https://github.com/hihi-team/pet-nunu-info/releases)**

---

## ❓ FAQ

**App có mã nguồn mở không?**
Bản build được phát hành công khai tại đây; mã nguồn giữ riêng tư. Repo này chỉ dùng để phân phối app.

**Bản Windows/Linux có đủ tính năng như macOS không?**
Dùng chung server, tài khoản, ví và format pet pack. Bản macOS (Swift) là bản gốc; bản Windows/Linux (Tauri) đang tiến tới parity đầy đủ.

**Có tốn phí không?**
Tải & dùng miễn phí. Một số vật phẩm trong app có thể mua bằng coin.

**Báo lỗi / góp ý?**
Mở **[Issue](https://github.com/hihi-team/pet-nunu-info/issues)** tại repo này.

---

<div align="center">
<sub>© hihiteam · Made with 🐾 for macOS · Windows · Linux</sub>
</div>
