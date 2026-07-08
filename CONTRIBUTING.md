Contributing to AEON Smart Home Guardian

ขอบคุณที่สนใจมีส่วนร่วมกับโครงการ AEON Smart Home Guardian และ AEON MATRIX

วิธีการมีส่วนร่วม

คุณสามารถมีส่วนร่วมได้โดย

- รายงานข้อบกพร่อง (Bug Reports)
- เสนอฟีเจอร์ใหม่ (Feature Requests)
- ปรับปรุงเอกสาร
- พัฒนาโค้ด
- เพิ่มชุดทดสอบ (Tests)
- ปรับปรุงประสิทธิภาพและความปลอดภัย

Workflow การพัฒนา

1. Fork หรือ Clone Repository
2. สร้าง Branch ใหม่

feature/<feature-name>
bugfix/<bug-name>
docs/<topic>
security/<topic>

3. พัฒนาและทดสอบโค้ด
4. Commit พร้อมข้อความที่สื่อความหมาย
5. Push ไปยัง Branch ของคุณ
6. เปิด Pull Request

แนวทางการ Commit

ใช้ข้อความ Commit ที่สื่อความหมาย เช่น

feat: add development intelligence engine
fix: resolve repository collector issue
docs: update architecture documentation
test: add unit tests for health engine
security: enable CodeQL workflow

Pull Request Checklist

ก่อนส่ง Pull Request โปรดตรวจสอบว่า

- โค้ดผ่าน Unit Tests
- โค้ดผ่าน Integration Tests (ถ้ามี)
- ไม่มี Secret หรือข้อมูลสำคัญใน Repository
- อัปเดตเอกสารที่เกี่ยวข้องแล้ว
- ตรวจสอบผลกระทบต่อระบบเรียบร้อยแล้ว

Coding Standards

- เขียนโค้ดให้อ่านง่าย
- ใช้ชื่อที่สื่อความหมาย
- เพิ่มความคิดเห็นเมื่อจำเป็น
- ลดการทำซ้ำของโค้ด
- ปฏิบัติตามมาตรฐานของภาษาและ Framework ที่ใช้

Security

- ห้าม Commit รหัสผ่าน API Keys หรือ Secrets
- ใช้ Environment Variables สำหรับข้อมูลสำคัญ
- รายงานช่องโหว่ด้านความปลอดภัยผ่านช่องทางที่กำหนดใน "SECURITY.md"

AI Governance

ทุกการเปลี่ยนแปลงที่เกี่ยวข้องกับ AI ควร

- สามารถตรวจสอบย้อนหลังได้
- มีเหตุผลและหลักฐานประกอบ
- ไม่ละเมิดนโยบายด้านความปลอดภัยและความเป็นส่วนตัว
- รองรับการกำกับดูแลโดยมนุษย์ (Human-in-the-Loop) เมื่อเหมาะสม

Code of Conduct

ผู้มีส่วนร่วมทุกคนต้องปฏิบัติตามข้อกำหนดใน "CODE_OF_CONDUCT.md"

ขอบคุณที่ร่วมพัฒนา AEON Smart Home Guardian ให้มีคุณภาพ ปลอดภัย และพร้อมใช้งานในระดับองค์กร
