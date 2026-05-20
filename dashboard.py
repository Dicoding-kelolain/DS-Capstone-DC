import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Kelola.in · Data Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .main {
        background: #080c14;
    }

    .block-container {
        padding: 1.5rem 2rem 3rem 2rem !important;
        max-width: 1400px;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1220 0%, #0a0f1a 100%) !important;
        border-right: 1px solid rgba(99, 179, 237, 0.12) !important;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div {
        font-family: 'DM Sans', sans-serif !important;
    }

    [data-testid="stSidebar"] button svg,
    [data-testid="stSidebar"] button [data-testid="stIconMaterial"] {
        font-family: "Material Symbols Rounded", "Material Icons" !important;
    }        
    
    [data-testid="stSidebarContent"] {
        padding: 1.5rem 1rem !important;
    }

    .nav-section-title {
        font-family: 'Syne', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: rgba(99, 179, 237, 0.5);
        padding: 1.2rem 0.5rem 0.4rem 0.5rem;
        margin-bottom: 0;
    }

    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 40%, #0f172a 100%);
        border: 1px solid rgba(99, 179, 237, 0.15);
        border-radius: 20px;
        padding: 36px 40px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }

    .hero-banner::before {
        content: '';
        position: absolute;
        top: -60px;
        right: -60px;
        width: 280px;
        height: 280px;
        background: radial-gradient(circle, rgba(99,179,237,0.12) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-banner::after {
        content: '';
        position: absolute;
        bottom: -80px;
        left: 30%;
        width: 220px;
        height: 220px;
        background: radial-gradient(circle, rgba(129,140,248,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }

    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: 2rem;
        font-weight: 800;
        color: #f1f5f9;
        margin: 0 0 6px 0;
        letter-spacing: -0.02em;
        position: relative;
        z-index: 1;
    }

    .hero-subtitle {
        font-size: 0.92rem;
        color: rgba(148, 163, 184, 0.8);
        margin: 0;
        position: relative;
        z-index: 1;
    }

    .hero-badge {
        display: inline-block;
        background: linear-gradient(90deg, rgba(99,179,237,0.2), rgba(129,140,248,0.2));
        border: 1px solid rgba(99,179,237,0.3);
        color: #93c5fd;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 999px;
        margin-bottom: 14px;
        position: relative;
        z-index: 1;
    }

    .kpi-card {
        background: linear-gradient(145deg, rgba(15,23,42,0.9), rgba(30,27,75,0.5));
        border: 1px solid rgba(99,179,237,0.14);
        border-radius: 16px;
        padding: 20px 18px;
        position: relative;
        overflow: hidden;
        transition: transform 0.2s, border-color 0.2s;
    }

    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99,179,237,0.3);
    }

    .kpi-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #63b3ed, #818cf8);
        border-radius: 16px 16px 0 0;
    }

    .kpi-icon {
        font-size: 1.5rem;
        margin-bottom: 10px;
        display: block;
    }

    .kpi-value {
        font-family: 'Syne', sans-serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: #e2e8f0;
        line-height: 1.1;
        word-break: break-word;
    }

    .kpi-label {
        font-size: 0.75rem;
        color: rgba(148,163,184,0.7);
        margin-top: 6px;
        line-height: 1.3;
        letter-spacing: 0.02em;
    }

    .section-title {
        font-family: 'Syne', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #e2e8f0;
        padding: 0 0 14px 0;
        margin: 0 0 2px 0;
        display: flex;
        align-items: center;
        gap: 8px;
        letter-spacing: -0.01em;
    }

    .section-title .dot {
        width: 6px;
        height: 6px;
        background: #63b3ed;
        border-radius: 50%;
        display: inline-block;
    }

    .insight-card {
        background: linear-gradient(135deg, rgba(99,179,237,0.06), rgba(129,140,248,0.06));
        border: 1px solid rgba(99,179,237,0.18);
        border-radius: 14px;
        padding: 18px 20px;
        margin: 16px 0;
        position: relative;
    }

    .insight-card::before {
        content: '💡';
        position: absolute;
        top: -12px;
        left: 16px;
        background: #0f172a;
        padding: 0 6px;
        font-size: 1rem;
    }

    .insight-card p {
        font-size: 0.875rem;
        color: rgba(203,213,225,0.85);
        margin: 0;
        line-height: 1.6;
    }

    .insight-card strong {
        color: #93c5fd;
    }

    .bq-header {
        background: linear-gradient(135deg, rgba(99,179,237,0.08), rgba(129,140,248,0.08));
        border: 1px solid rgba(99,179,237,0.18);
        border-left: 3px solid #63b3ed;
        border-radius: 0 14px 14px 0;
        padding: 16px 20px;
        margin-bottom: 24px;
    }

    .bq-header .bq-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #63b3ed;
        margin-bottom: 6px;
    }

    .bq-header .bq-text {
        font-size: 0.9rem;
        color: rgba(203,213,225,0.85);
        line-height: 1.5;
        margin: 0;
    }

    .custom-divider {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99,179,237,0.2), transparent);
        margin: 24px 0;
    }

    .mini-metric {
        flex: 1;
        min-width: 120px;
        background: rgba(15,23,42,0.8);
        border: 1px solid rgba(99,179,237,0.12);
        border-radius: 12px;
        padding: 14px 16px;
        text-align: center;
    }

    .mini-metric .val {
        font-family: 'Syne', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        color: #93c5fd;
    }

    .mini-metric .lbl {
        font-size: 0.72rem;
        color: rgba(148,163,184,0.65);
        margin-top: 4px;
    }

    .stSlider > label, .stSelectbox > label, .stDateInput > label {
        font-size: 0.82rem !important;
        color: rgba(148,163,184,0.8) !important;
        font-weight: 500 !important;
    }

    .stSuccess {
        background: rgba(34,197,94,0.08) !important;
        border: 1px solid rgba(34,197,94,0.2) !important;
        border-radius: 10px !important;
        color: #4ade80 !important;
        font-size: 0.85rem !important;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(15,23,42,0.6) !important;
        border-radius: 12px;
        padding: 4px;
        border: 1px solid rgba(99,179,237,0.1);
        gap: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        padding: 8px 18px !important;
        font-size: 0.82rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        color: rgba(148,163,184,0.7) !important;
        background: transparent !important;
    }

    .stTabs [aria-selected="true"] {
        background: rgba(99,179,237,0.12) !important;
        color: #93c5fd !important;
        font-weight: 600 !important;
    }

    .js-plotly-plot {
        border-radius: 12px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PLOTLY TEMPLATE
# ─────────────────────────────────────────────
CHART_THEME = "plotly_dark"
CHART_BG = "rgba(0,0,0,0)"
CHART_PAPER_BG = "rgba(0,0,0,0)"
FONT_COLOR = "#94a3b8"
GRID_COLOR = "rgba(99,179,237,0.07)"
ACCENT = "#63b3ed"
ACCENT2 = "#818cf8"
ACCENT3 = "#34d399"

def base_layout(extra=None):
    layout = dict(
        template=CHART_THEME,
        plot_bgcolor=CHART_BG,
        paper_bgcolor=CHART_PAPER_BG,
        font=dict(family="DM Sans", color=FONT_COLOR, size=11),
        margin=dict(l=16, r=16, t=24, b=40),
        xaxis=dict(gridcolor=GRID_COLOR, zeroline=False, tickfont=dict(size=10)),
        yaxis=dict(gridcolor=GRID_COLOR, zeroline=False, tickfont=dict(size=10)),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=10)),
        hoverlabel=dict(
            bgcolor="#1e293b",
            font_family="DM Sans",
            font_size=12,
            bordercolor="rgba(99,179,237,0.3)"
        ),
    )

    if extra:
        layout.update(extra)

    return layout

# ─────────────────────────────────────────────
# DATA LOADING
# ─────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data():
    url_tx = "dataset/transactions_clean.csv"
    url_inv = "dataset/inventory_clean.csv"
    url_fin = "dataset/financials_clean.csv"

    # Transactions
    df_tx = pd.read_csv(url_tx)
    df_tx.columns = df_tx.columns.str.lower().str.replace(" ", "_")

    if "invoice_id" not in df_tx.columns and "invoice" in df_tx.columns:
        df_tx["invoice_id"] = df_tx["invoice"]

    if "invoice_date" in df_tx.columns:
        df_tx["invoice_date"] = pd.to_datetime(df_tx["invoice_date"], errors="coerce")

    for col in ["quantity", "unit_price", "sales_amount"]:
        if col in df_tx.columns:
            df_tx[col] = pd.to_numeric(df_tx[col], errors="coerce")

    if "sales_amount" not in df_tx.columns and {"quantity", "unit_price"}.issubset(df_tx.columns):
        df_tx["sales_amount"] = df_tx["quantity"] * df_tx["unit_price"]

    if "invoice_date" in df_tx.columns:
        df_tx["month_year"] = df_tx["invoice_date"].dt.to_period("M").astype(str)
        df_tx["day_name"] = df_tx["invoice_date"].dt.day_name()
        df_tx["week"] = df_tx["invoice_date"].dt.isocalendar().week.astype("Int64")

    # Inventory
    df_inv = pd.read_csv(url_inv)
    df_inv.columns = df_inv.columns.str.lower().str.replace(" ", "_").str.replace("/", "_")

    if "date" in df_inv.columns:
        df_inv["date"] = pd.to_datetime(df_inv["date"], errors="coerce")

    for col in [
        "units_sold",
        "units_ordered",
        "inventory_level",
        "demand_forecast",
        "price",
        "discount",
        "competitor_pricing",
    ]:
        if col in df_inv.columns:
            df_inv[col] = pd.to_numeric(df_inv[col], errors="coerce")

    if "demand_forecast" in df_inv.columns:
        df_inv["demand_forecast"] = df_inv["demand_forecast"].clip(lower=0)

    # Financials
    df_fin = pd.read_csv(url_fin)
    df_fin.columns = df_fin.columns.str.lower().str.replace(" ", "_")

    if "order_date" in df_fin.columns:
        df_fin["order_date"] = pd.to_datetime(df_fin["order_date"], errors="coerce")

    for col in ["quantity", "price", "revenue"]:
        if col in df_fin.columns:
            df_fin[col] = pd.to_numeric(df_fin[col], errors="coerce")

    if "revenue" not in df_fin.columns and {"quantity", "price"}.issubset(df_fin.columns):
        df_fin["revenue"] = df_fin["quantity"] * df_fin["price"]

    if "order_date" in df_fin.columns:
        df_fin["month_year"] = df_fin["order_date"].dt.to_period("M").astype(str)

    return df_tx, df_inv, df_fin

# ─────────────────────────────────────────────
# LOAD DATA OUTSIDE SIDEBAR
# ─────────────────────────────────────────────
with st.spinner("Memuat data…"):
    df_tx, df_inv, df_fin = load_data()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 12px 0 20px'>
        <div style='font-family:Syne,sans-serif; font-size:1.4rem; font-weight:800; color:#e2e8f0; letter-spacing:-0.02em;'>
            Kelola.in
        </div>
        <div style='font-size:0.72rem; color:rgba(99,179,237,0.6); letter-spacing:0.12em; text-transform:uppercase; margin-top:4px;'>
            Data Analysis
        </div>
    </div>
    <hr style='border:none; height:1px; background:rgba(99,179,237,0.12); margin:0 0 12px;'>
    """, unsafe_allow_html=True)

    page_options = {
        "🏠 Overview & EDA": "overview",
        "❓ Q1 · Diskon Produk Unggulan": "q1",
        "❓ Q2 · Risiko Stockout": "q2",
        "❓ Q3 · Clearance Strategy": "q3",
        "❓ Q4 · Bundling & Restock": "q4",
        "❓ Q5 · Pola Mingguan": "q5",
    }

    if "active_page" not in st.session_state:
        st.session_state.active_page = "overview"

    st.markdown('<div class="nav-section-title">Navigasi</div>', unsafe_allow_html=True)

    for label, key in page_options.items():
        active = st.session_state.active_page == key

        if st.button(
            label,
            key=f"nav_{key}",
            use_container_width=True,
            type="primary" if active else "secondary",
        ):
            st.session_state.active_page = key
            st.rerun()

    st.markdown('<div class="nav-section-title">Filter Global</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div style='
        background: rgba(15,23,42,0.7);
        border: 1px solid rgba(99,179,237,0.12);
        border-radius: 12px;
        padding: 12px 14px;
        margin: 10px 0 16px 0;
        font-size: 0.72rem;
        color: rgba(203,213,225,0.75);
        line-height: 1.8;
    '>
        <b style='color:#93c5fd;'>Dataset Loaded</b><br>
        Transaksi: <b style='color:#63b3ed'>{len(df_tx):,}</b><br>
        Inventori: <b style='color:#63b3ed'>{len(df_inv):,}</b><br>
        Keuangan: <b style='color:#63b3ed'>{len(df_fin):,}</b>
    </div>
    """, unsafe_allow_html=True)

    valid_dates = df_tx["invoice_date"].dropna()

    min_date = valid_dates.min().date()
    max_date = valid_dates.max().date()

    date_range = st.date_input(
        "Rentang Tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(date_range) == 2:
        df_tx_f = df_tx[
            (df_tx["invoice_date"].dt.date >= date_range[0]) &
            (df_tx["invoice_date"].dt.date <= date_range[1])
        ].copy()
    else:
        df_tx_f = df_tx.copy()

    if "category" in df_inv.columns:
        cats = ["Semua"] + sorted(df_inv["category"].dropna().unique().tolist())
        sel_cat_inv = st.selectbox("Kategori Inventori", cats)
        df_inv_f = df_inv[df_inv["category"] == sel_cat_inv].copy() if sel_cat_inv != "Semua" else df_inv.copy()
    else:
        df_inv_f = df_inv.copy()

    if "category" in df_fin.columns:
        cats_fin = ["Semua"] + sorted(df_fin["category"].dropna().unique().tolist())
        sel_cat_fin = st.selectbox("Kategori Keuangan", cats_fin)
        df_fin_f = df_fin[df_fin["category"] == sel_cat_fin].copy() if sel_cat_fin != "Semua" else df_fin.copy()
    else:
        df_fin_f = df_fin.copy()

    st.markdown("---")
    st.markdown(f"""
    <div style='font-size:0.72rem; color:rgba(148,163,184,0.5); padding:4px 0; line-height:1.8;'>
        Transaksi aktif: <b style='color:#63b3ed'>{len(df_tx_f):,}</b><br>
        Inventori: <b style='color:#63b3ed'>{len(df_inv_f):,}</b><br>
        Keuangan: <b style='color:#63b3ed'>{len(df_fin_f):,}</b>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# COMPUTED KPIs
# ─────────────────────────────────────────────
invoice_col = "invoice_id" if "invoice_id" in df_tx_f.columns else "invoice"

total_rev_tx = df_tx_f["sales_amount"].sum()
total_rev_fin = df_fin_f["revenue"].sum()
total_orders = df_tx_f[invoice_col].nunique() if invoice_col in df_tx_f.columns else 0
total_products = df_tx_f["description"].nunique() if "description" in df_tx_f.columns else 0
avg_order_value = total_rev_tx / total_orders if total_orders > 0 else 0

page = st.session_state.active_page

# ═════════════════════════════════════════════
# PAGE: OVERVIEW & EDA
# ═════════════════════════════════════════════
if page == "overview":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Streamlit Analisis Data</div>
        <h1 class="hero-title">OVERVIEW DASHBOARD</h1>
        <p class="hero-subtitle">
            Hasil analisis dataset transaksi, inventori, dan keuangan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    kpi_data = [
        ("💰", f"$ {total_rev_tx:,.0f}".replace(",", "."), "Revenue Transaksi"),
        ("📈", f"$ {total_rev_fin:,.0f}".replace(",", "."), "Revenue Keuangan"),
        ("🧾", f"{total_orders:,}", "Total Invoice"),
        ("📦", f"{total_products:,}", "Produk Unik"),
        ("🎯", f"$ {avg_order_value:,.0f}", "Avg per Invoice"),
    ]

    cols = st.columns(5)

    for col, (icon, val, lbl) in zip(cols, kpi_data):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-value">{val}</div>
                <div class="kpi-label">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    eda_tabs = st.tabs(["📅 Tren Waktu", "📦 Inventori", "💰 Keuangan", "🔍 Preview Data"])

    with eda_tabs[0]:
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(
                '<div class="section-title"><span class="dot"></span>Revenue Bulanan — Transaksi</div>',
                unsafe_allow_html=True
            )

            monthly_tx = (
                df_tx_f.groupby("month_year")["sales_amount"]
                .sum()
                .reset_index()
                .sort_values("month_year")
            )

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=monthly_tx["month_year"],
                y=monthly_tx["sales_amount"],
                mode="lines+markers",
                line=dict(color=ACCENT, width=2.5),
                marker=dict(size=6, color=ACCENT, line=dict(color="#0f172a", width=2)),
                fill="tozeroy",
                fillcolor="rgba(99,179,237,0.07)",
                name="Sales"
            ))

            fig.update_layout(**base_layout({
                "xaxis_tickangle": -35,
                "xaxis_title": "",
                "yaxis_title": ""
            }))

            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.markdown(
                '<div class="section-title"><span class="dot"></span>Revenue Bulanan — Keuangan</div>',
                unsafe_allow_html=True
            )

            monthly_fin = (
                df_fin_f.groupby("month_year")["revenue"]
                .sum()
                .reset_index()
                .sort_values("month_year")
            )

            fig2 = go.Figure()

            fig2.add_trace(go.Scatter(
                x=monthly_fin["month_year"],
                y=monthly_fin["revenue"],
                mode="lines+markers",
                line=dict(color=ACCENT3, width=2.5),
                marker=dict(size=6, color=ACCENT3, line=dict(color="#0f172a", width=2)),
                fill="tozeroy",
                fillcolor="rgba(52,211,153,0.07)",
                name="Revenue"
            ))

            fig2.update_layout(**base_layout({
                "xaxis_tickangle": -35
            }))

            st.plotly_chart(fig2, use_container_width=True)

        c3, c4 = st.columns(2)

        with c3:
            st.markdown(
                '<div class="section-title"><span class="dot"></span>Penjualan per Hari dalam Seminggu</div>',
                unsafe_allow_html=True
            )

            day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day_labels = ["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"]

            sales_day = (
                df_tx_f.groupby("day_name")["sales_amount"]
                .sum()
                .reindex(day_order)
                .reset_index()
            )

            colors_bar = [ACCENT if i < 5 else ACCENT2 for i in range(7)]

            fig3 = go.Figure(go.Bar(
                x=day_labels,
                y=sales_day["sales_amount"],
                marker_color=colors_bar,
                marker_line_width=0,
                text=[f"{v/1e3:.0f}K" for v in sales_day["sales_amount"].fillna(0)],
                textposition="outside",
                textfont=dict(size=9, color=FONT_COLOR),
            ))

            fig3.update_layout(**base_layout({
                "bargap": 0.35
            }))

            st.plotly_chart(fig3, use_container_width=True)

        with c4:
            st.markdown(
                '<div class="section-title"><span class="dot"></span>Revenue per Kategori</div>',
                unsafe_allow_html=True
            )

            if "category" in df_fin_f.columns:
                rev_cat = (
                    df_fin_f.groupby("category")["revenue"]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )

                fig4 = go.Figure(go.Pie(
                    labels=rev_cat["category"],
                    values=rev_cat["revenue"],
                    hole=0.55,
                    marker=dict(colors=["#63b3ed", "#818cf8", "#34d399", "#f59e0b", "#f87171", "#a78bfa"]),
                    textinfo="label+percent",
                    textfont=dict(size=10),
                    insidetextorientation="radial",
                ))

                fig4.update_layout(**base_layout({
                    "showlegend": False
                }))

                st.plotly_chart(fig4, use_container_width=True)

    with eda_tabs[1]:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Units Sold vs Units Ordered per Kategori</div>',
            unsafe_allow_html=True
        )

        if "category" in df_inv_f.columns and "units_sold" in df_inv_f.columns and "units_ordered" in df_inv_f.columns:
            inv_cat = (
                df_inv_f.groupby("category")[["units_sold", "units_ordered"]]
                .sum()
                .reset_index()
                .melt(id_vars="category", var_name="Metric", value_name="Total")
            )

            fig5 = px.bar(
                inv_cat,
                x="category",
                y="Total",
                color="Metric",
                barmode="group",
                color_discrete_map={"units_sold": ACCENT, "units_ordered": "#f87171"},
                template=CHART_THEME,
            )

            fig5.update_layout(**base_layout({
                "bargap": 0.2,
                "bargroupgap": 0.05
            }))

            st.plotly_chart(fig5, use_container_width=True)

        if "demand_forecast" in df_inv_f.columns and "inventory_level" in df_inv_f.columns:
            c1, c2 = st.columns(2)

            with c1:
                st.markdown(
                    '<div class="section-title"><span class="dot"></span>Distribusi Inventory Level</div>',
                    unsafe_allow_html=True
                )

                fig_hist = go.Figure(go.Histogram(
                    x=df_inv_f["inventory_level"].dropna(),
                    nbinsx=40,
                    marker_color=ACCENT,
                    opacity=0.75,
                ))

                fig_hist.update_layout(**base_layout())
                st.plotly_chart(fig_hist, use_container_width=True)

            with c2:
                st.markdown(
                    '<div class="section-title"><span class="dot"></span>Demand Forecast per Kategori</div>',
                    unsafe_allow_html=True
                )

                if "category" in df_inv_f.columns:
                    fc_cat = (
                        df_inv_f.groupby("category")["demand_forecast"]
                        .mean()
                        .sort_values(ascending=False)
                        .reset_index()
                    )

                    fig_fc = go.Figure(go.Bar(
                        x=fc_cat["category"],
                        y=fc_cat["demand_forecast"],
                        marker_color=ACCENT3,
                        marker_line_width=0,
                    ))

                    fig_fc.update_layout(**base_layout())
                    st.plotly_chart(fig_fc, use_container_width=True)

    with eda_tabs[2]:
        if "category" in df_fin_f.columns:
            c1, c2 = st.columns(2)

            with c1:
                st.markdown(
                    '<div class="section-title"><span class="dot"></span>Revenue Distribution per Kategori</div>',
                    unsafe_allow_html=True
                )

                fig_box = px.box(
                    df_fin_f.dropna(subset=["revenue", "category"]),
                    x="category",
                    y="revenue",
                    color="category",
                    color_discrete_sequence=["#63b3ed", "#818cf8", "#34d399", "#f59e0b", "#f87171", "#a78bfa"],
                    template=CHART_THEME,
                )

                fig_box.update_layout(**base_layout({
                    "showlegend": False
                }))

                st.plotly_chart(fig_box, use_container_width=True)

            with c2:
                st.markdown(
                    '<div class="section-title"><span class="dot"></span>Revenue vs Quantity Scatter</div>',
                    unsafe_allow_html=True
                )

                sample_df = df_fin_f.dropna(subset=["revenue", "quantity"]).sample(
                    min(2000, len(df_fin_f)),
                    random_state=42
                )

                fig_sc = px.scatter(
                    sample_df,
                    x="quantity",
                    y="revenue",
                    color="category" if "category" in df_fin_f.columns else None,
                    opacity=0.55,
                    template=CHART_THEME,
                    color_discrete_sequence=["#63b3ed", "#818cf8", "#34d399", "#f59e0b", "#f87171", "#a78bfa"],
                )

                fig_sc.update_layout(**base_layout({
                    "showlegend": True
                }))

                st.plotly_chart(fig_sc, use_container_width=True)

    with eda_tabs[3]:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Preview Dataset</div>',
            unsafe_allow_html=True
        )

        with st.expander("📄 Transactions"):
            st.dataframe(df_tx_f.head(100), use_container_width=True)

        with st.expander("📦 Inventory"):
            st.dataframe(df_inv_f.head(100), use_container_width=True)

        with st.expander("💰 Financials"):
            st.dataframe(df_fin_f.head(100), use_container_width=True)

# ═════════════════════════════════════════════
# PAGE Q1
# ═════════════════════════════════════════════
elif page == "q1":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Business Question 01</div>
        <h1 class="hero-title">🏷️ Diskon Produk Unggulan</h1>
        <p class="hero-subtitle">
            Identifikasi top 20% produk penyumbang revenue dan simulasi dampak diskon pada hari penjualan terendah.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bq-header">
        <div class="bq-label">Pertanyaan Bisnis</div>
        <p class="bq-text">
            Produk apa yang termasuk dalam top 20% penyumbang pendapatan selama periode yang dipilih,
            dan berapa peningkatan penjualan yang dapat dicapai jika diberikan diskon pada periode penjualan terendah?
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([2, 1])

    with c1:
        lookback = st.slider("Periode Analisis (hari)", 30, 180, 90, step=10)

    with c2:
        discount_pct = st.slider("Simulasi Diskon (%)", 5, 30, 10, step=5)

    latest_date = df_tx_f["invoice_date"].max()
    df_90 = df_tx_f[df_tx_f["invoice_date"] >= (latest_date - pd.Timedelta(days=lookback))].copy()

    product_rev = (
        df_90.groupby("description")["sales_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    product_rev["revenue_pct"] = product_rev["sales_amount"] / product_rev["sales_amount"].sum() * 100
    product_rev["cumulative_pct"] = product_rev["revenue_pct"].cumsum()

    top20 = product_rev[product_rev["cumulative_pct"] <= 20].copy()

    cols = st.columns(3)

    metric_q1 = [
        (cols[0], f"{len(top20)}", "Produk Top 20%"),
        (cols[1], f"$ {top20['sales_amount'].sum():,.0f}".replace(",", "."), "Revenue"),
        (cols[2], f"{top20['sales_amount'].sum() / product_rev['sales_amount'].sum() * 100:.1f}%", "Share Revenue"),
    ]

    for col, val, lbl in metric_q1:
        with col:
            st.markdown(f"""
            <div class="mini-metric">
                <div class="val">{val}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Top Produk Penyumbang 20% Revenue</div>',
            unsafe_allow_html=True
        )

        fig_q1a = go.Figure(go.Bar(
            x=top20.head(15)["sales_amount"],
            y=top20.head(15)["description"],
            orientation="h",
            marker=dict(
                color=top20.head(15)["sales_amount"],
                colorscale=[[0, "#1e3a5f"], [0.5, ACCENT], [1, "#93c5fd"]],
                line=dict(width=0),
            ),
            text=[f"$ {v/1e3:.0f}K" for v in top20.head(15)["sales_amount"]],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_q1a.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"},
            "xaxis_title": "Sales Amount",
        }))

        st.plotly_chart(fig_q1a, use_container_width=True)

    with c2:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Penjualan per Hari</div>',
            unsafe_allow_html=True
        )

        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_labels_id = {
            "Monday": "Senin",
            "Tuesday": "Selasa",
            "Wednesday": "Rabu",
            "Thursday": "Kamis",
            "Friday": "Jumat",
            "Saturday": "Sabtu",
            "Sunday": "Minggu"
        }

        df_90["day_name"] = df_90["invoice_date"].dt.day_name()

        sales_day_90 = (
            df_90.groupby("day_name")["sales_amount"]
            .sum()
            .reindex(day_order)
            .reset_index()
        )

        lowest_day = sales_day_90.dropna(subset=["sales_amount"]).loc[sales_day_90["sales_amount"].idxmin()]

        colors = [
            "#ef4444" if d == lowest_day["day_name"] else ACCENT
            for d in sales_day_90["day_name"]
        ]

        fig_q1b = go.Figure(go.Bar(
            x=[day_labels_id.get(d, d) for d in sales_day_90["day_name"]],
            y=sales_day_90["sales_amount"],
            marker_color=colors,
            marker_line_width=0,
        ))

        fig_q1b.update_layout(**base_layout({
            "bargap": 0.32
        }))

        st.plotly_chart(fig_q1b, use_container_width=True)

    st.markdown(
        '<div class="section-title"><span class="dot"></span>Simulasi Peningkatan Penjualan dengan Diskon</div>',
        unsafe_allow_html=True
    )

    base = lowest_day["sales_amount"]
    discount2 = min(discount_pct + 5, 30)

    sim_data = pd.DataFrame({
        "Skenario": ["Tanpa Diskon", f"Diskon {discount_pct}%", f"Diskon {discount2}%"],
        "Estimasi Sales": [
            base,
            base * (1 + discount_pct / 100),
            base * (1 + discount2 / 100)
        ],
        "color": [FONT_COLOR, ACCENT, ACCENT2],
    })

    fig_sim = go.Figure(go.Bar(
        x=sim_data["Skenario"],
        y=sim_data["Estimasi Sales"],
        marker_color=sim_data["color"],
        marker_line_width=0,
        text=[f"$ {v:,.0f}" for v in sim_data["Estimasi Sales"]],
        textposition="outside",
        textfont=dict(size=10),
    ))

    fig_sim.update_layout(**base_layout({
        "bargap": 0.5,
        "yaxis_title": "Estimasi Sales"
    }))

    st.plotly_chart(fig_sim, use_container_width=True)

    st.markdown(f"""
    <div class="insight-card">
        <p>
        Hari penjualan terendah adalah <strong>{day_labels_id.get(lowest_day['day_name'], lowest_day['day_name'])}</strong>
        dengan total sales <strong>Rp {base:,.0f}</strong>. Pemberian diskon <strong>{discount_pct}%</strong>
        diestimasi meningkatkan penjualan menjadi <strong>Rp {base*(1+discount_pct/100):,.0f}</strong>.
        Strategi diskon pada hari sepi dapat memaksimalkan revenue dari produk unggulan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Tabel Produk Top 20%"):
        st.dataframe(
            top20.style.format({
                "sales_amount": "Rp {:,.2f}",
                "revenue_pct": "{:.2f}%",
                "cumulative_pct": "{:.2f}%"
            }),
            use_container_width=True
        )

# ═════════════════════════════════════════════
# PAGE Q2
# ═════════════════════════════════════════════
elif page == "q2":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Business Question 02</div>
        <h1 class="hero-title">⚠️ Risiko Stockout</h1>
        <p class="hero-subtitle">
            Produk mana yang akan kehabisan stok paling cepat dan berapa restock optimal untuk menjaga ketersediaan?
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bq-header">
        <div class="bq-label">Pertanyaan Bisnis</div>
        <p class="bq-text">
            Produk mana yang memiliki rata-rata penjualan harian tertinggi dan akan mengalami kehabisan stok dalam batas hari tertentu jika tidak dilakukan restock?
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        lookback_inv = st.slider("Periode Analisis (hari)", 14, 90, 30, step=7, key="inv_days")

    with c2:
        stockout_threshold = st.slider("Ambang Batas Stockout (hari)", 3, 14, 7, key="stockout_thresh")

    with c3:
        restock_days = st.slider("Target Stok (hari ke depan)", 7, 30, 14, key="restock_days")

    latest_inv = df_inv_f["date"].max()
    df_inv_30 = df_inv_f[df_inv_f["date"] >= (latest_inv - pd.Timedelta(days=lookback_inv))].copy()

    stockout = (
        df_inv_30.groupby(["product_id", "category"])
        .agg(
            units_sold=("units_sold", "sum"),
            inventory_level=("inventory_level", "mean")
        )
        .reset_index()
    )

    stockout["avg_daily_sales"] = stockout["units_sold"] / lookback_inv
    stockout["days_until_stockout"] = stockout["inventory_level"] / stockout["avg_daily_sales"].replace(0, np.nan)
    stockout["recommended_restock"] = (
        stockout["avg_daily_sales"] * restock_days - stockout["inventory_level"]
    ).clip(lower=0)

    stockout["risk_level"] = stockout["days_until_stockout"].apply(
        lambda x: "Kritis" if x <= 3 else ("Sedang" if x <= stockout_threshold else "Aman")
    )

    at_risk = stockout[
        stockout["days_until_stockout"] <= stockout_threshold
    ].sort_values("days_until_stockout")

    cols = st.columns(3)

    metric_q2 = [
        (cols[0], f"{len(at_risk)}", "Produk Berisiko Stockout"),
        (cols[1], f"{at_risk['days_until_stockout'].mean():.1f} hari", "Rata-rata Hari Tersisa"),
        (cols[2], f"{at_risk['recommended_restock'].sum():,.0f}", "Unit Perlu Direstock"),
    ]

    for col, val, lbl in metric_q2:
        with col:
            st.markdown(f"""
            <div class="mini-metric">
                <div class="val">{val}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Produk Risiko Stockout</div>',
            unsafe_allow_html=True
        )

        color_map = {
            "Kritis": "#ef4444",
            "Sedang": "#f59e0b",
            "Aman": "#22c55e"
        }

        fig_stock = px.bar(
            at_risk.head(15),
            x="days_until_stockout",
            y="product_id",
            orientation="h",
            color="risk_level",
            color_discrete_map=color_map,
            template=CHART_THEME,
        )

        fig_stock.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"},
            "showlegend": True
        }))

        st.plotly_chart(fig_stock, use_container_width=True)

    with c2:
        st.markdown(
            f'<div class="section-title"><span class="dot"></span>Rekomendasi Restock ({restock_days} Hari)</div>',
            unsafe_allow_html=True
        )

        fig_restock = go.Figure(go.Bar(
            x=at_risk.head(15)["recommended_restock"],
            y=at_risk.head(15)["product_id"],
            orientation="h",
            marker=dict(
                color=at_risk.head(15)["recommended_restock"],
                colorscale=[[0, "#7c3aed"], [1, ACCENT2]],
                line=dict(width=0),
            ),
            text=[f"{v:.0f} unit" for v in at_risk.head(15)["recommended_restock"]],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_restock.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"}
        }))

        st.plotly_chart(fig_restock, use_container_width=True)

    st.markdown(
        '<div class="section-title"><span class="dot"></span>Penjualan Harian vs Risiko Stockout</div>',
        unsafe_allow_html=True
    )

    fig_scatter = px.scatter(
        stockout.dropna(subset=["days_until_stockout"]),
        x="avg_daily_sales",
        y="days_until_stockout",
        color="category",
        size="recommended_restock",
        template=CHART_THEME,
        opacity=0.75,
        color_discrete_sequence=["#63b3ed", "#818cf8", "#34d399", "#f59e0b", "#f87171", "#a78bfa"],
        hover_data=["product_id"],
    )

    fig_scatter.add_hline(
        y=stockout_threshold,
        line_dash="dot",
        line_color="#ef4444",
        annotation_text=f"Batas Risiko ({stockout_threshold} hari)",
        annotation_font_color="#ef4444",
        annotation_font_size=10,
    )

    fig_scatter.update_layout(**base_layout())
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown(f"""
    <div class="insight-card">
        <p>
        Terdapat <strong>{len(at_risk)} produk</strong> yang berisiko mengalami stockout dalam ≤{stockout_threshold} hari.
        Total unit yang perlu dipesan adalah <strong>{at_risk['recommended_restock'].sum():,.0f} unit</strong>
        untuk memenuhi kebutuhan <strong>{restock_days} hari</strong> ke depan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Tabel Analisis Stockout"):
        st.dataframe(
            at_risk.style.format({
                "avg_daily_sales": "{:.2f}",
                "inventory_level": "{:.2f}",
                "days_until_stockout": "{:.2f}",
                "recommended_restock": "{:.0f}",
            }),
            use_container_width=True
        )

# ═════════════════════════════════════════════
# PAGE Q3
# ═════════════════════════════════════════════
elif page == "q3":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Business Question 03</div>
        <h1 class="hero-title">🏪 Clearance Strategy</h1>
        <p class="hero-subtitle">
            Identifikasi produk slow-moving dan hitung potensi pemulihan nilai melalui diskon clearance.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bq-header">
        <div class="bq-label">Pertanyaan Bisnis</div>
        <p class="bq-text">
            Produk apa yang memiliki penjualan di bawah rata-rata dan bagaimana strategi clearance dapat membantu mengurangi stok lambat?
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        lb60 = st.slider("Periode Analisis (hari)", 30, 120, 60, step=10, key="q3_days")

    with c2:
        clearance_pct = st.slider("Diskon Clearance (%)", 10, 50, 25, step=5, key="q3_disc")

    latest_date = df_tx_f["invoice_date"].max()
    df_60 = df_tx_f[df_tx_f["invoice_date"] >= (latest_date - pd.Timedelta(days=lb60))].copy()

    prod_sales_60 = (
        df_60.groupby("description")["sales_amount"]
        .sum()
        .reset_index()
    )

    avg_sales = prod_sales_60["sales_amount"].mean()

    below_avg = (
        prod_sales_60[prod_sales_60["sales_amount"] < avg_sales]
        .sort_values("sales_amount")
        .copy()
    )

    below_avg["clearance_discount"] = below_avg["sales_amount"] * (clearance_pct / 100)
    below_avg["sales_after_clearance"] = below_avg["sales_amount"] - below_avg["clearance_discount"]

    below_avg["performance"] = below_avg["sales_amount"].apply(
        lambda x: "Sangat Rendah" if x < avg_sales * 0.1 else "Di Bawah Rata-rata"
    )

    cols = st.columns(3)

    metric_q3 = [
        (cols[0], f"{len(below_avg)}", "Produk di Bawah Rata-rata"),
        (cols[1], f"$ {avg_sales:,.0f}".replace(",", "."), "Rata-rata Penjualan"),
        (cols[2], f"$ {below_avg['clearance_discount'].sum():,.0f}".replace(",", "."), "Estimasi Pemulihan"),
    ]

    for col, val, lbl in metric_q3:
        with col:
            st.markdown(f"""
            <div class="mini-metric">
                <div class="val">{val}</div>
                <div class="lbl">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>20 Produk Penjualan Terendah</div>',
            unsafe_allow_html=True
        )

        worst20 = below_avg.head(20).copy()

        fig_below = go.Figure(go.Bar(
            x=worst20["sales_amount"],
            y=worst20["description"],
            orientation="h",
            marker_color=[
                "#ef4444" if p == "Sangat Rendah" else "#f59e0b"
                for p in worst20["performance"]
            ],
            marker_line_width=0,
        ))

        fig_below.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"}
        }))

        st.plotly_chart(fig_below, use_container_width=True)

    with c2:
        st.markdown(
            f'<div class="section-title"><span class="dot"></span>Estimasi Pemulihan dengan Diskon {clearance_pct}%</div>',
            unsafe_allow_html=True
        )

        total_before = below_avg["sales_amount"].sum()
        total_after = below_avg["sales_after_clearance"].sum()

        fig_comp = go.Figure(go.Bar(
            x=["Tanpa Diskon", f"Dengan Diskon {clearance_pct}%"],
            y=[total_before, total_after],
            marker_color=["#475569", ACCENT3],
            marker_line_width=0,
            text=[f"$ {v:,.0f}" for v in [total_before, total_after]],
            textposition="outside",
            textfont=dict(size=10),
        ))

        fig_comp.update_layout(**base_layout({
            "bargap": 0.55
        }))

        st.plotly_chart(fig_comp, use_container_width=True)

    st.markdown(
        '<div class="section-title"><span class="dot"></span>Distribusi Produk Berdasarkan Performa Penjualan</div>',
        unsafe_allow_html=True
    )

    bins = [0, avg_sales * 0.1, avg_sales * 0.5, avg_sales, float("inf")]
    labels_bin = [
        "Sangat Rendah (<10%)",
        "Rendah (10–50%)",
        "Di Bawah Rata-rata (50–100%)",
        "Di Atas Rata-rata"
    ]

    prod_sales_60_copy = prod_sales_60.copy()
    prod_sales_60_copy["segment"] = pd.cut(
        prod_sales_60_copy["sales_amount"],
        bins=bins,
        labels=labels_bin
    )

    seg_count = prod_sales_60_copy["segment"].value_counts().reset_index()
    seg_count.columns = ["Segment", "Jumlah"]

    fig_seg = go.Figure(go.Pie(
        labels=seg_count["Segment"],
        values=seg_count["Jumlah"],
        hole=0.5,
        marker_colors=["#ef4444", "#f59e0b", "#eab308", "#22c55e"],
        textinfo="label+percent",
        textfont=dict(size=10),
    ))

    fig_seg.update_layout(**base_layout({
        "showlegend": False
    }))

    st.plotly_chart(fig_seg, use_container_width=True)

    st.markdown(f"""
    <div class="insight-card">
        <p>
        Terdapat <strong>{len(below_avg)} produk</strong> dengan penjualan di bawah rata-rata
        (<strong>Rp {avg_sales:,.0f}</strong>). Diskon clearance <strong>{clearance_pct}%</strong>
        dapat membantu memulihkan nilai sebesar <strong>Rp {below_avg['clearance_discount'].sum():,.0f}</strong>
        dari produk yang stagnan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Data Produk Slow-Moving"):
        st.dataframe(
            below_avg.head(50).style.format({
                "sales_amount": "Rp {:,.3f}",
                "clearance_discount": "Rp {:,.3f}",
                "sales_after_clearance": "Rp {:,.3f}",
            }),
            use_container_width=True
        )

# ═════════════════════════════════════════════
# PAGE Q4
# ═════════════════════════════════════════════
elif page == "q4":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Business Question 04</div>
        <h1 class="hero-title">🎁 Bundling & Restock Optimization</h1>
        <p class="hero-subtitle">
            Kombinasi produk revenue tinggi dan perputaran stok untuk strategi bundling terbaik.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bq-header">
        <div class="bq-label">Pertanyaan Bisnis</div>
        <p class="bq-text">
            Bagaimana kombinasi produk dengan penjualan tinggi dan tingkat perputaran stok dapat digunakan untuk menentukan strategi bundling dan restock?
        </p>
    </div>
    """, unsafe_allow_html=True)

    top_n = st.slider("Tampilkan Top N Produk", 5, 30, 15, key="q4_topn")

    high_rev = (
        df_tx_f.groupby("description")["sales_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )

    inv_turn = (
        df_inv_f.groupby(["product_id", "category"])
        .agg(
            units_sold=("units_sold", "sum"),
            inventory_level=("inventory_level", "mean")
        )
        .reset_index()
    )

    inv_turn["turnover_ratio"] = inv_turn["units_sold"] / inv_turn["inventory_level"].replace(0, np.nan)
    high_turn = inv_turn.sort_values("turnover_ratio", ascending=False).head(top_n)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Produk Revenue Tertinggi</div>',
            unsafe_allow_html=True
        )

        fig_hr = go.Figure(go.Bar(
            x=high_rev["sales_amount"],
            y=high_rev["description"],
            orientation="h",
            marker=dict(
                color=high_rev["sales_amount"],
                colorscale=[[0, "#1e3a5f"], [1, "#93c5fd"]],
                line=dict(width=0),
            ),
            text=[f"$ {v/1e3:.0f}K" for v in high_rev["sales_amount"]],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_hr.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"}
        }))

        st.plotly_chart(fig_hr, use_container_width=True)

    with c2:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Turnover Inventori Tertinggi</div>',
            unsafe_allow_html=True
        )

        fig_ht = px.bar(
            high_turn,
            x="turnover_ratio",
            y="product_id",
            orientation="h",
            color="category",
            template=CHART_THEME,
            color_discrete_sequence=["#63b3ed", "#818cf8", "#34d399", "#f59e0b", "#f87171", "#a78bfa"],
        )

        fig_ht.update_layout(**base_layout({
            "yaxis": {"autorange": "reversed"},
            "showlegend": True
        }))

        st.plotly_chart(fig_ht, use_container_width=True)

    if "category" in df_fin_f.columns:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Revenue & Avg Price per Kategori</div>',
            unsafe_allow_html=True
        )

        rev_cat = df_fin_f.groupby("category")["revenue"].sum().reset_index()
        qty_cat = df_fin_f.groupby("category")["quantity"].sum().reset_index()

        merged_cat = rev_cat.merge(qty_cat, on="category")
        merged_cat["avg_price"] = merged_cat["revenue"] / merged_cat["quantity"].replace(0, np.nan)

        fig_cat = make_subplots(
            rows=1,
            cols=2,
            subplot_titles=["Total Revenue", "Avg Price"]
        )

        fig_cat.add_trace(
            go.Bar(
                x=merged_cat["category"],
                y=merged_cat["revenue"],
                marker_color=ACCENT,
                marker_line_width=0,
                name="Revenue"
            ),
            row=1,
            col=1
        )

        fig_cat.add_trace(
            go.Bar(
                x=merged_cat["category"],
                y=merged_cat["avg_price"],
                marker_color=ACCENT2,
                marker_line_width=0,
                name="Avg Price"
            ),
            row=1,
            col=2
        )

        fig_cat.update_layout(
            template=CHART_THEME,
            plot_bgcolor=CHART_BG,
            paper_bgcolor=CHART_PAPER_BG,
            font=dict(family="DM Sans", color=FONT_COLOR, size=11),
            margin=dict(l=16, r=16, t=40, b=60),
            showlegend=False,
        )

        st.plotly_chart(fig_cat, use_container_width=True)

    if "demand_forecast" in df_inv_f.columns and "category" in df_inv_f.columns:
        st.markdown(
            '<div class="section-title"><span class="dot"></span>Demand Forecast per Kategori</div>',
            unsafe_allow_html=True
        )

        fc_cat = (
            df_inv_f.groupby("category")["demand_forecast"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig_fc = go.Figure(go.Bar(
            x=fc_cat["category"],
            y=fc_cat["demand_forecast"],
            marker_color=ACCENT3,
            marker_line_width=0,
            text=[f"{v:.1f}" for v in fc_cat["demand_forecast"]],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_fc.update_layout(**base_layout({
            "bargap": 0.4
        }))

        st.plotly_chart(fig_fc, use_container_width=True)

    st.markdown("""
    <div class="insight-card">
        <p>
        Produk dengan <strong>revenue tinggi</strong> dan <strong>turnover ratio tinggi</strong>
        adalah kandidat ideal untuk strategi bundling. Bundling produk best-seller dengan produk slow-mover
        dapat meningkatkan perputaran stok sekaligus menjaga revenue.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Data Turnover Inventori"):
        st.dataframe(
            high_turn.style.format({
                "turnover_ratio": "{:.2f}",
                "inventory_level": "{:.2f}"
            }),
            use_container_width=True
        )

# ═════════════════════════════════════════════
# PAGE Q5
# ═════════════════════════════════════════════
elif page == "q5":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Business Question 05</div>
        <h1 class="hero-title">📅 Pola Permintaan Mingguan</h1>
        <p class="hero-subtitle">
            Distribusi penjualan produk terlaris berdasarkan hari untuk perencanaan stok.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="bq-header">
        <div class="bq-label">Pertanyaan Bisnis</div>
        <p class="bq-text">
            Bagaimana distribusi penjualan produk terlaris berdasarkan hari dalam seminggu,
            dan apakah pola tersebut dapat digunakan sebagai dasar perencanaan stok?
        </p>
    </div>
    """, unsafe_allow_html=True)

    top_products_list = (
        df_tx_f.groupby("description")["sales_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
        .index
        .tolist()
    )

    selected_product = st.selectbox("Pilih Produk untuk Dianalisis", top_products_list)

    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day_labels_id = {
        "Monday": "Senin",
        "Tuesday": "Selasa",
        "Wednesday": "Rabu",
        "Thursday": "Kamis",
        "Friday": "Jumat",
        "Saturday": "Sabtu",
        "Sunday": "Minggu"
    }

    day_labels = [day_labels_id[d] for d in day_order]

    df_sel = df_tx_f[df_tx_f["description"] == selected_product].copy()

    prod_day = (
        df_sel.groupby("day_name")
        .agg(
            quantity=("quantity", "sum"),
            sales_amount=("sales_amount", "sum")
        )
        .reindex(day_order)
        .reset_index()
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f'<div class="section-title"><span class="dot"></span>Quantity per Hari: {selected_product[:40]}</div>',
            unsafe_allow_html=True
        )

        peak_idx = prod_day["quantity"].idxmax()
        peak_day = prod_day.loc[peak_idx, "day_name"] if not pd.isna(prod_day.loc[peak_idx, "quantity"]) else None

        colors_p = [
            "#fbbf24" if d == peak_day else ACCENT
            for d in prod_day["day_name"]
        ]

        fig_day = go.Figure(go.Bar(
            x=day_labels,
            y=prod_day["quantity"],
            marker_color=colors_p,
            marker_line_width=0,
            text=[
                f"{v:.0f}" if not pd.isna(v) else ""
                for v in prod_day["quantity"]
            ],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_day.update_layout(**base_layout({
            "bargap": 0.32
        }))

        st.plotly_chart(fig_day, use_container_width=True)

    with c2:
        st.markdown(
            f'<div class="section-title"><span class="dot"></span>Sales Amount per Hari: {selected_product[:40]}</div>',
            unsafe_allow_html=True
        )

        fig_day2 = go.Figure(go.Bar(
            x=day_labels,
            y=prod_day["sales_amount"],
            marker=dict(
                color=prod_day["sales_amount"].fillna(0),
                colorscale=[[0, "#3b0764"], [1, ACCENT2]],
                line=dict(width=0),
            ),
            text=[
                f"$ {v/1e3:.1f}K" if not pd.isna(v) else ""
                for v in prod_day["sales_amount"]
            ],
            textposition="outside",
            textfont=dict(size=9, color=FONT_COLOR),
        ))

        fig_day2.update_layout(**base_layout({
            "bargap": 0.32
        }))

        st.plotly_chart(fig_day2, use_container_width=True)

    st.markdown(
        '<div class="section-title"><span class="dot"></span>Heatmap Penjualan Mingguan — Top 10 Produk</div>',
        unsafe_allow_html=True
    )

    top10 = (
        df_tx_f.groupby("description")["sales_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .index
        .tolist()
    )

    df_top10 = df_tx_f[df_tx_f["description"].isin(top10)].copy()

    pivot = (
        df_top10.groupby(["description", "day_name"])["quantity"]
        .sum()
        .unstack(fill_value=0)
        .reindex(columns=day_order, fill_value=0)
    )

    pivot.columns = day_labels

    fig_heat = go.Figure(go.Heatmap(
        z=pivot.values,
        x=day_labels,
        y=[d[:30] for d in pivot.index.tolist()],
        colorscale=[[0, "#0f172a"], [0.4, "#1e3a5f"], [0.7, ACCENT], [1, "#93c5fd"]],
        hovertemplate="Produk: %{y}<br>Hari: %{x}<br>Qty: %{z}<extra></extra>",
    ))

    fig_heat.update_layout(**base_layout({
        "height": 360
    }))

    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown(
        '<div class="section-title"><span class="dot"></span>Tren Penjualan Mingguan Keseluruhan</div>',
        unsafe_allow_html=True
    )

    overall_day = (
        df_tx_f.groupby("day_name")["sales_amount"]
        .sum()
        .reindex(day_order)
        .reset_index()
    )

    fig_overall = go.Figure()

    fig_overall.add_trace(go.Scatter(
        x=day_labels,
        y=overall_day["sales_amount"],
        mode="lines+markers",
        line=dict(color="#fbbf24", width=3),
        marker=dict(size=8, color="#fbbf24", line=dict(color="#0f172a", width=2)),
        fill="tozeroy",
        fillcolor="rgba(251,191,36,0.08)",
        name="Total Sales"
    ))

    fig_overall.update_layout(**base_layout())
    st.plotly_chart(fig_overall, use_container_width=True)

    valid_overall = overall_day.dropna(subset=["sales_amount"])

    peak_overall = valid_overall.loc[
        valid_overall["sales_amount"].idxmax(),
        "day_name"
    ]

    low_overall = valid_overall.loc[
        valid_overall["sales_amount"].idxmin(),
        "day_name"
    ]

    st.markdown(f"""
    <div class="insight-card">
        <p>
        Hari penjualan tertinggi secara keseluruhan adalah
        <strong>{day_labels_id.get(peak_overall, peak_overall)}</strong>
        dan terendah adalah
        <strong>{day_labels_id.get(low_overall, low_overall)}</strong>.
        Untuk produk <strong>{selected_product[:50]}</strong>, peak demand terjadi pada hari
        <strong>{day_labels_id.get(peak_day, peak_day) if peak_day else '-'}</strong>.
        Pola ini dapat dijadikan dasar perencanaan stok mingguan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📋 Tabel Penjualan Harian Produk Terpilih"):
        prod_day_display = prod_day.copy()
        prod_day_display["day_name"] = prod_day_display["day_name"].map(day_labels_id)

        st.dataframe(
            prod_day_display.style.format({
                "quantity": "{:,.0f}",
                "sales_amount": "Rp {:,.2f}",
            }),
            use_container_width=True
        )

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style='text-align:center; color:rgba(99,179,237,0.3); font-size:0.75rem; padding:32px 0 8px; letter-spacing:0.08em;'>
    KELOLA.IN · Interactive Dashboard · Capstone Project - CC26-PSU248 · Dataset: Transactions · Inventory · Financials
</div>
""", unsafe_allow_html=True)