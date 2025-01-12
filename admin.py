from flask import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_h')
def admin_h():
    return render_template('admin_h.html')