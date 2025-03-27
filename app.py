from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)
COUPONS_FILE = 'coupons.json'

def load_coupons():
    if not os.path.exists(COUPONS_FILE):
        return []
    
    with open(COUPONS_FILE, 'r') as f:
        coupons = json.load(f)
    
    # Filter out expired coupons and add display date
    today = datetime.now().date()
    valid_coupons = []
    
    for coupon in coupons:
        try:
            expiry_date = datetime.strptime(coupon['expiry_date'], '%Y-%m-%d').date()
            if expiry_date >= today:  # Only keep valid coupons
                coupon['display_date'] = expiry_date.strftime('%d/%m/%Y')
                valid_coupons.append(coupon)
        except:
            # If date parsing fails, keep the coupon but don't add display_date
            valid_coupons.append(coupon)
    
    # Save back the filtered list
    if len(valid_coupons) != len(coupons):
        with open(COUPONS_FILE, 'w') as f:
            json.dump(valid_coupons, f, indent=2)
    
    return valid_coupons

def save_coupons(coupons):
    with open(COUPONS_FILE, 'w') as f:
        json.dump(coupons, f, indent=2)

@app.route('/')
def index():
    coupons = load_coupons()
    today = datetime.now().date()
    
    # Create expiring soon list with original indices
    expiring_soon = []
    for index, coupon in enumerate(coupons):
        try:
            expiry_date = datetime.strptime(coupon['expiry_date'], '%Y-%m-%d').date()
            if 0 <= (expiry_date - today).days <= 3:
                # Store both coupon data and its original index
                expiring_soon.append({
                    'coupon': coupon,
                    'original_index': index
                })
        except:
            continue
    
    return render_template('index.html', coupons=coupons, expiring_soon=expiring_soon)

@app.route('/add', methods=['GET', 'POST'])
def add_coupon():
    if request.method == 'POST':
        coupon_type = request.form['type']
        expiry_date = request.form['expiry_date']
        
        coupon_data = {
            'type': coupon_type,
            'expiry_date': expiry_date
        }
        
        if coupon_type == '15%':
            coupon_data['code'] = request.form['code']
        elif coupon_type == '20%':
            coupon_data['survey_code'] = request.form['survey_code']
            coupon_data['id'] = request.form['id']
        else:
            coupon_data['other_info'] = request.form['other_info']
        
        coupons = load_coupons()
        coupons.append(coupon_data)
        save_coupons(coupons)
        
        return redirect(url_for('index'))
    
    return render_template('addcoupon.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_coupon(index):
    coupons = load_coupons()
    
    if request.method == 'POST':
        coupon_type = request.form['type']
        expiry_date = request.form['expiry_date']
        
        coupon_data = {
            'type': coupon_type,
            'expiry_date': expiry_date
        }
        
        if coupon_type == '15%':
            coupon_data['code'] = request.form['code']
        elif coupon_type == '20%':
            coupon_data['survey_code'] = request.form['survey_code']
            coupon_data['id'] = request.form['id']
        else:
            coupon_data['other_info'] = request.form['other_info']
        
        coupons[index] = coupon_data
        save_coupons(coupons)
        
        return redirect(url_for('index'))
    
    coupon = coupons[index]
    return render_template('editcoupon.html', coupon=coupon, index=index)

@app.route('/delete/<int:index>')
def delete_coupon(index):
    coupons = load_coupons()
    del coupons[index]
    save_coupons(coupons)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085)
