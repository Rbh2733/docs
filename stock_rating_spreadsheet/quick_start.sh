#!/bin/bash
# Quick Start Script for Automated Stock Rating System

echo "🚀 Stock Rating System - Quick Start"
echo "===================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

echo "✓ pip3 found"
echo ""

# Install requirements
echo "📦 Installing required packages..."
echo ""
pip3 install -q yfinance pandas numpy openpyxl schedule 2>&1 | grep -v "already satisfied" || true
echo ""
echo "✓ Packages installed"
echo ""

# Run the automation
echo "🤖 Running automated stock rating..."
echo ""
python3 auto_stock_rater.py

echo ""
echo "✅ Done!"
echo ""
echo "📊 Check these files:"
echo "   - dashboard.html (open in browser)"
echo "   - tier*_scores_*.csv (spreadsheet data)"
echo ""
echo "💡 Next steps:"
echo "   1. Edit watchlist.json to add your stocks"
echo "   2. Run 'python3 auto_stock_rater.py' anytime for updates"
echo "   3. Set up automation: 'python3 scheduler.py --mode daily --time 09:30'"
echo ""
echo "📖 Read AUTOMATION_GUIDE.md for full documentation"
