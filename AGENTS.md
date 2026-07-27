# pet-nunu-info — Rules

Repo **công khai** để phát hành & phân phối Petnunu Desktop (macOS · Windows ·
Linux). Chứa: README 22 ngôn ngữ, GitHub Releases (binary + `appcast.xml` +
`latest.json`), và nhật ký cập nhật. **Không** chứa mã nguồn app (source private).

## `changelog/` — nguồn sự thật của nhật ký cập nhật

Nguồn sự thật là **thư mục `changelog/`**: mỗi bản phát hành **một file JSON**.
File `changelog.json` ở root là **bản build tự sinh — đừng sửa tay**.

Vì sao vẫn phải có file build ở root: web đọc nhật ký **lúc chạy** qua
`https://raw.githubusercontent.com/hihi-team/pet-nunu-info/main/changelog.json`
(xem `web/src/community/useChangelog.ts` trong repo `petnunu-f27`), mà `raw`
không liệt kê được nội dung thư mục — liệt kê bằng GitHub API thì dính giới hạn
60 request/giờ cho khách ẩn danh. Sai định dạng = trang changelog hỏng.

Tên file:
- Bản có số: `changelog/1.2.0.json`.
- Mốc chưa đánh số: `changelog/2026-07-25-windows-linux.json` (ngày + slug ngắn).

```json
// changelog/1.2.0.json
{
  "version": "1.2.0",              // tuỳ chọn — bỏ ở mốc phát triển chưa đánh số
  "date": "2026-07-27",            // BẮT BUỘC — ISO yyyy-mm-dd
  "seq": 1,                        // tuỳ chọn — xem "Thứ tự" bên dưới
  "title": { "en": "…", "vi": "…" },   // BẮT BUỘC — "en" bắt buộc
  "note":  { "en": "…", "vi": "…" },   // tuỳ chọn — ghi chú ngắn dưới tiêu đề
  "entries": [                     // BẮT BUỘC — ít nhất 1 mục
    { "kind": "new",     "text": { "en": "…", "vi": "…" } },
    { "kind": "improve", "text": { "en": "…", "vi": "…" } },
    { "kind": "fix",     "text": { "en": "…", "vi": "…" } }
  ]
}
```

Quy ước:
- `kind` chỉ nhận `new` | `improve` | `fix`.
- Mỗi chuỗi đa ngôn ngữ (`title`/`note`/`text`) **bắt buộc có `en`**; `vi` nên
  có. Locale khác thiếu → web tự rơi về `en` (giống chính sách trang pháp lý:
  chỉ en/vi là bản gốc). Muốn thêm bản dịch ngôn ngữ khác thì thêm khoá locale
  vào đúng object đó, ví dụ `"ja": "…"`.
- Viết theo **góc nhìn người dùng**, không dùng mã feature nội bộ (F19, F22…).

**Thứ tự** trong bản build: mới→cũ theo `date`; **cùng ngày** thì `seq` lớn hơn
đứng trước (`seq` mặc định 0). Chỉ cần `seq` khi trong một ngày có từ hai bản
trở lên. `seq` là chuyện xếp thứ tự nội bộ nên bị **loại khỏi** bản build.

## Sửa changelog → chạy script build → commit cả hai

```sh
python3 scripts/build_changelog.py          # sinh lại changelog.json ở root
python3 scripts/build_changelog.py --check  # chỉ so, không ghi (CI dùng)
```

Script kiểm luôn định dạng (thiếu `en`, `kind` lạ, JSON hỏng → báo tên file và
thoát mã 1). GitHub Action `.github/workflows/changelog.yml` chạy `--check` mỗi
lần đụng `changelog/` — quên build là CI đỏ, không bao giờ lệch âm thầm.

## Rule bắt buộc: phát hành = việc của HAI repo

Repo này (public) giữ changelog + GitHub Release. Repo **`hihi-team/pet-nunu-desktop`**
(private) giữ mã nguồn + workflow build. User nói "đánh version 1.2.0 / phát
hành bản mới" là kích hoạt cả checklist dưới đây, ở cả hai bên:

1. **[repo source]** Version bằng nhau ở 6 chỗ: `ProPetMac.xcodeproj`
   (`MARKETING_VERSION`), `desktop/package.json`, `desktop/src-tauri/tauri.conf.json`,
   `desktop/Cargo.toml`, `web/package.json`, `server/Cargo.toml`.
2. **[repo NÀY, làm TRƯỚC]** Thêm `changelog/<version>.json` (en + vi tối thiểu),
   chạy `python3 scripts/build_changelog.py`, commit **cả file nguồn lẫn
   `changelog.json` build**, push `main`.
3. **[repo source]** `git tag -a v<version> -m "…" && git push origin v<version>`
   — `.github/workflows/release.yml` chỉ chạy khi có tag `v*`.
4. **[tự động]** Job `publish` của workflow đó tạo Release `v<version>` **trên
   repo này** (title `Petnunu <version>`) rồi upload file cài 3 nền tảng +
   `appcast.xml` (Sparkle, macOS) + `latest.json` (updater Tauri).

Tiêu đề GitHub Release và changelog phải cùng kể một câu chuyện. Web tự đồng bộ
— không cần sửa gì bên `petnunu-f27/web`.

Hỏng âm thầm hay gặp: đúng version mà **quên bước 2** → trang "Có gì mới" lệch
bản thật đang phát hành; đúng changelog mà **quên bước 3** → CI không build gì,
user không có bản nào để tải.
