from flask import Flask, request, jsonify

app = Flask(__name__)

# ==========================
# 1. 统一认证接口（来自 01-统一认证.md）
# ==========================
@app.route("/login", methods=["POST"])
def login():
    return jsonify({"code": 200, "msg": "环境校验通过"})

@app.route("/getLoginUser", methods=["GET"])
def getLoginUser():
    # 漏洞：未授权访问
    return jsonify({
        "code": 200,
        "msg": "success",
        "data": {
            "userId": "2023001",
            "userName": "测试学生",
            "deptName": "计算机学院",
            "roleType": "student",
            "isLogin": True
        }
    })

@app.route("/getUserPermissionRouters", methods=["GET"])
def getUserPermissionRouters():
    # 漏洞：垂直越权
    return jsonify({
        "code": 200,
        "data": [
            {"path": "/home", "title": "首页"},
            {"path": "/course", "title": "我的课表"},
            {"path": "/admin", "title": "后台管理"}
        ]
    })

@app.route("/SYS_CARD_PERSONALDATA", methods=["GET"])
def SYS_CARD_PERSONALDATA():
    return jsonify({
        "code": 200,
        "data": {
            "stuId": "2023001",
            "realName": "测试学生",
            "college": "计算机学院",
            "major": "网络安全",
            "grade": "2023级"
        }
    })

# ==========================
# 2. 教务系统接口（来自 02-教务系统认证.md）
# ==========================
@app.route("/zdpz_cxZdpzList.html", methods=["POST"])
def zdpz_cxZdpzList():
    # 漏洞：水平越权
    zd_fzdm = request.form.get("zd_fzdm", "")
    return jsonify({
        "code": 200,
        "data": {
            "studentId": zd_fzdm,
            "courseName": "网络安全",
            "score": 95,
            "term": "2023-2024-2"
        }
    })

@app.route("/bjkbdy_cxKbzdxsxx.html", methods=["GET"])
def bjkbdy_cxKbzdxsxx():
    return jsonify({
        "code": 200,
        "data": {
            "courseName": "Web安全",
            "classRoom": "计算机楼305",
            "teacher": "李老师",
            "time": "周一 1-2节"
        }
    })

@app.route("/cdjy_cxXqjc.html", methods=["GET"])
def cdjy_cxXqjc():
    return jsonify({
        "code": 200,
        "data": [{"classRoom": "305", "status": "空闲"}, {"classRoom": "306", "status": "空闲"}]
    })

# ==========================
# 3. 学工系统接口（来自 03-学工系统认证.md）
# ==========================
@app.route("/leaveSchool.do", methods=["POST"])
def leaveSchool():
    return jsonify({"code": 200, "data": {"status": "审批通过", "studentId": "2023001"}})

@app.route("/zhcptybbapp.do", methods=["POST"])
def zhcptybbapp():
    return jsonify({"code": 200, "data": {"score": "90", "level": "优秀"}})

@app.route("/apply.do", methods=["POST"])
def apply():
    # 漏洞：金额可篡改
    return jsonify({"code": 200, "data": {"amount": 5000, "status": "审核中"}})

@app.route("/getViolateExamine.do", methods=["POST"])
def getViolateExamine():
    return jsonify({"code": 200, "data": {"record": "无违纪"}})

@app.route("/jjrlfxapp.do", methods=["POST"])
def jjrlfxapp():
    return jsonify({"code": 200, "data": {"status": "已登记"}})

@app.route("/hdsb.do", methods=["POST"])
def hdsb():
    return jsonify({"code": 200, "data": {"activity": "网络安全竞赛", "status": "报名成功"}})

@app.route("/wdqj.do", methods=["POST"])
def wdqj():
    return jsonify({"code": 200, "data": {"status": "待审核"}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)