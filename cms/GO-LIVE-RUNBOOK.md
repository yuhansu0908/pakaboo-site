# 帕咔布官網後台（CMS）— 使用與上線說明

讓團隊**不用碰程式碼**，登入網頁填表單就能：① 發布**最新消息**文章、② 公告**活動・講座**、③ 更新**園區照片**。架構跟 Emotion Design 那套一樣（Decap CMS + GitHub + Cloudflare Pages + DecapBridge 登入）。

---

## 一、資料夾結構

```
Pakaboo Website/                ← 這整個資料夾＝GitHub repo 的內容
├─ index / about / courses / life / contact .html   原始 5 頁
├─ assets/        site.css, site.js, logo.png, 課程圖, menu.jpg
│   └─ uploads/   ← 後台上傳的照片存這裡
└─ cms/
    ├─ admin/         後台介面（Decap CMS）
    │   ├─ index.html
    │   └─ config.yml ← 後台欄位設定（上線前要填 repo 與登入站台 ID）
    ├─ content/
    │   ├─ news/*.md      最新消息（每篇一個檔）
    │   ├─ events/*.md    活動・講座（每場一個檔）
    │   └─ gallery.yml    園區照片清單
    ├─ build.py       產生器：讀 content/ → 產生整包網站到 build/
    └─ build/         ← 實際要部署的成品（自動產生，勿手改）
```

## 二、後台有哪三個功能

| 後台選項 | 對應網頁 | 欄位 |
|---|---|---|
| **最新消息** | `news.html` 列表 ＋ 各篇文章頁 | 標題、日期、封面（可空）、摘要、置頂、內文 |
| **活動・講座** | `events.html`（即將舉行／已結束自動分區） | 名稱、類型(活動/講座)、日期、時間、地點、封面、簡介、報名連結、詳情 |
| **園區照片** | 注入「園區生活 → 環境實景」 | 一張張照片＋說明文字（留空＝顯示預設版位） |

> 導覽列與頁尾會自動多出「最新消息」「活動・講座」兩個入口。

## 三、本機預覽（測試用）

```
cd "Pakaboo Website/cms"
python3 build.py          # 需要 pyyaml：pip install pyyaml
```

成品在 `cms/build/`，雙擊 `cms/build/index.html` 即可預覽整站（含新聞、活動頁）。

本機要登入後台測試，可在 `admin/config.yml` 最上面**暫時**加一行 `local_backend: true`，並另開 `npx decap-server`；正式上線用下面的設定。

## 四、上線（一次性設定，照做即可）

> 你 Emotion 那站已經走過同樣流程，這裡是帕卡布版。

### 1) 建 GitHub repo
- 開一個 repo，例如 `pakaboo-site`（Private 即可）。
- 把 **Pakaboo Website 整個資料夾的內容**推上去（index.html、assets/、cms/ 都要）。

### 2) 設定登入服務 DecapBridge
- 到 DecapBridge 新增一個 site，綁定上面的 GitHub repo。
- 取得該 site 的 **ID**，填回 `cms/admin/config.yml`：
  - `repo: 你的帳號/pakaboo-site`
  - `auth_endpoint` / `auth_token_endpoint` 裡的 `REPLACE_WITH_DECAPBRIDGE_SITE_ID` 換成實際 ID。
- 在 DecapBridge 後台**邀請團隊成員 email**，他們就能登入。

### 3) Cloudflare Pages 接上自動建置
- Cloudflare → Workers & Pages → **Create → Pages → 連接 GitHub** → 選 `pakaboo-site`。
- 建置設定：
  - **Build command**：`pip install pyyaml && python3 cms/build.py`
  - **Build output directory**：`cms/build`
- Deploy。之後綁自訂網域（例如 `pakaboo.iamhanhan.com` 或你要的網址）。

### 4) 完成
- 團隊開 `你的網址/admin/` → 用 email 登入 → 新增/編輯內容 → **Publish**。
- 一按發布＝對 GitHub commit ＝ Cloudflare 自動重新 `build.py` ＝ 幾分鐘後線上更新。**沒有人需要碰程式碼。**

## 五、團隊日常怎麼用

- **發最新消息**：後台 → 最新消息 → New → 填標題/日期/內文（要圖就上傳封面）→ Publish。
- **公告活動/講座**：後台 → 活動・講座 → New → 選類型、填日期時間地點 → Publish。日期過了會自動移到「已結束」。
- **換園區照片**：後台 → 園區照片 → 在清單裡新增照片、填說明 → Publish。環境實景就會換成實拍照。

## 六、注意
- 照片上傳會存到 `assets/uploads/`，跟著 repo 一起版本控管。
- 「園區照片」清單留空時，網頁顯示預設的 8 格版位，不會出錯。
- `cms/build/` 是自動產生的，**不要手動改**；要改版型改原始 5 頁或 `assets/site.css`、`cms/build.py`。
- 本機無法代你建立 GitHub／DecapBridge／Cloudflare 帳號或推送，上述帳號相關步驟需你在自己的瀏覽器操作（跟 Emotion 那次一樣）。
