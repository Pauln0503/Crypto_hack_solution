
# 📘 README – ECDSA (Elliptic Curve Digital Signature Algorithm)

## 1. Giới thiệu

**ECDSA** là viết tắt của *Elliptic Curve Digital Signature Algorithm* – một thuật toán chữ ký số dựa trên **đường cong elliptic**. Nó là phiên bản của DSA (Digital Signature Algorithm) nhưng thay vì dựa trên số nguyên lớn (modular exponentiation), nó dùng toán học của **elliptic curve cryptography (ECC)**.

Ưu điểm:

* 🔒 Bảo mật mạnh với kích thước khóa nhỏ hơn so với RSA/DSA.
* ⚡ Nhanh hơn (tạo chữ ký & xác minh).
* 📱 Rất phù hợp cho thiết bị hạn chế tài nguyên (IoT, mobile, blockchain).

Ứng dụng thực tế: **Bitcoin, Ethereum, TLS/SSL, SSH, JWT, chứng chỉ số…**

---

## 2. Thành phần chính của ECDSA

### Các tham số công khai (public parameters)

* **Elliptic curve**: Được xác định bởi phương trình $y^2 = x^3 + ax + b$ trên trường hữu hạn $\mathbb{F}_p$.
* **Generator point (G)**: một điểm sinh trên đường cong.
* **Order (n)**: số lần nhân G cho đến khi quay lại điểm vô cực.
* **Field size (p)**: modulus của trường số nguyên.

### Khóa

* **Private key (d)**: một số nguyên bí mật $d \in [1, n-1]$.
* **Public key (Q)**: $Q = d \cdot G$ (nhân điểm trên elliptic curve).

---

## 3. Thuật toán chữ ký số ECDSA

### 📌 Ký một thông điệp

Cho thông điệp $m$:

1. Tính hash:

   $$
   e = \text{HASH}(m)
   $$
2. Chọn số ngẫu nhiên $k \in [1, n-1]$. (**k phải bí mật, không được tái sử dụng**).
3. Tính:

   $$
   R = k \cdot G = (x, y)
   $$

   lấy $r = x \bmod n$.
   Nếu $r = 0$, chọn k khác.
4. Tính:

   $$
   s = k^{-1} \cdot (e + d \cdot r) \bmod n
   $$

   Nếu $s = 0$, chọn k khác.
5. Chữ ký = cặp $(r, s)$.

---

### 📌 Xác minh chữ ký

Cho thông điệp $m$, chữ ký $(r, s)$, và public key $Q$:

1. Kiểm tra $1 \leq r, s \leq n-1$.
2. Tính hash:

   $$
   e = \text{HASH}(m)
   $$
3. Tính nghịch đảo:

   $$
   w = s^{-1} \bmod n
   $$
4. Tính:

   $$
   u_1 = e \cdot w \bmod n, \quad u_2 = r \cdot w \bmod n
   $$
5. Tính điểm:

   $$
   P = u_1 \cdot G + u_2 \cdot Q
   $$

   Nếu $P = (x, y)$, lấy $v = x \bmod n$.
6. Chữ ký hợp lệ nếu $v = r$.

---

## 4. Điểm yếu & Lưu ý bảo mật

* 🚨 Nếu **tái sử dụng k**, hoặc k bị lộ → private key $d$ sẽ bị tính ngược.
* 🚨 Nếu random không đủ entropy (ví dụ Sony PS3 từng dính lỗi ECDSA với k cố định = 1).
* 🚨 Phải dùng hàm hash chuẩn (SHA-256, SHA-3).

---

## 5. Ví dụ ngắn (minh họa)

Giả sử:

* Curve: secp192k1 (generator G, order n).
* Private key: $d = 12345$.
* Public key: $Q = d \cdot G$.

Ký:

```
m = "Hello"
hash = SHA1(m)
k = 67890
R = k*G = (x, y)
r = x mod n
s = (hash + d*r) * k^{-1} mod n
```

Chữ ký = (r, s).

Xác minh: bên nhận dùng $Q$, hash(m), r, s → tính toán và so khớp.

---

## 6. Ứng dụng thực tế

* **Blockchain (Bitcoin, Ethereum)**: mọi giao dịch đều ký bằng ECDSA.
* **TLS/SSL**: chứng chỉ số với ECDSA.
* **SSH**: hỗ trợ khóa ECDSA thay vì RSA.
* **JWT (JSON Web Token)**: chuẩn ES256, ES384, ES512.

---

## 7. Tài liệu tham khảo

* [NIST FIPS 186-4: Digital Signature Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf)
* [SEC 1: Elliptic Curve Cryptography](https://www.secg.org/sec1-v2.pdf)
* [Wikipedia – ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)

---

