{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2827df8-25c1-4910-b63a-1fd6915952df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [02/Dec/2025 13:29:14] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:29:15] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m4s\u001b[0m 4s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:30:15] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 1s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:31:04] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 545ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:31:43] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 397ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:31:57] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:33:05] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:33:05] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 562ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:34:45] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:35:01] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 550ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:35:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:39:15] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:43:03] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 518ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:43:19] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 731ms/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:43:41] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:50:03] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:50:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:50:55] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:51:20] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:51:52] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:52:24] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:54:46] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 13:56:11] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m2s\u001b[0m 2s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 13:57:00] \"POST /predict HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 14:52:29] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [02/Dec/2025 14:57:03] \"GET / HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m244s\u001b[0m 244s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 14:58:31] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m16s\u001b[0m 16s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 14:58:32] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m5s\u001b[0m 5s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 15:00:46] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 1s/step\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [02/Dec/2025 16:53:25] \"POST /predict HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, jsonify\n",
    "import tensorflow as tf\n",
    "from tensorflow.keras.models import load_model\n",
    "from tensorflow.keras.preprocessing.image import img_to_array\n",
    "from PIL import Image\n",
    "import numpy as np\n",
    "import os\n",
    "from werkzeug.utils import secure_filename\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.config['UPLOAD_FOLDER'] = 'uploads'\n",
    "app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB\n",
    "ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}\n",
    "\n",
    "os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)\n",
    "\n",
    "model = load_model('cat_dog_vgg16_model.keras')\n",
    "\n",
    "def allowed_file(filename):\n",
    "    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS\n",
    "\n",
    "def prepare_image(image_path, target_size=(128, 128)):\n",
    "    img = Image.open(image_path)\n",
    "    img = img.convert('RGB')\n",
    "    img = img.resize(target_size)\n",
    "    img_array = img_to_array(img)\n",
    "    img_array = img_array / 255.0\n",
    "    img_array = np.expand_dims(img_array, axis=0)\n",
    "    return img_array\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    if 'file' not in request.files:\n",
    "        return jsonify({'error': 'Aucun fichier trouvé'}), 400\n",
    "    \n",
    "    file = request.files['file']\n",
    "    \n",
    "    if file.filename == '':\n",
    "        return jsonify({'error': 'Aucun fichier sélectionné'}), 400\n",
    "    \n",
    "    if file and allowed_file(file.filename):\n",
    "        filename = secure_filename(file.filename)\n",
    "        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)\n",
    "        file.save(filepath)\n",
    "        \n",
    "        try:\n",
    "            img_array = prepare_image(filepath, target_size=(128, 128))\n",
    "            prediction = model.predict(img_array)\n",
    "            result = float(prediction[0][0])\n",
    "            \n",
    "            if result > 0.5:\n",
    "                label = 'Chien'\n",
    "                confidence = result * 100\n",
    "            else:\n",
    "                label = 'Chat'\n",
    "                confidence = (1 - result) * 100\n",
    "            \n",
    "            os.remove(filepath)\n",
    "            \n",
    "            return jsonify({\n",
    "                'prediction': label,\n",
    "                'confidence': f'{confidence:.2f}%',\n",
    "                'raw_score': result\n",
    "            })\n",
    "        \n",
    "        except Exception as e:\n",
    "            if os.path.exists(filepath):\n",
    "                os.remove(filepath)\n",
    "            return jsonify({'error': str(e)}), 500\n",
    "    \n",
    "    return jsonify({'error': 'Type de fichier non autorisé'}), 400\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d2a103e-ad68-4c71-a50e-202871549918",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (tf_cpu)",
   "language": "python",
   "name": "tf_cpu"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
