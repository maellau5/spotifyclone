from flask import Blueprint, request, jsonify
from models import db, User, Song, Playlist
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@api.route('/songs', methods=['GET'])
def get_songs():
    songs = Song.query.all()
    songs_list = [{'id': song.id, 'title': song.title, 'artist': song.artist, 'url': song.url} for song in songs]
    return jsonify(songs_list), 200

@api.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    new_playlist = Playlist(name=name, user_id=user_id)
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created successfully', 'playlist_id': new_playlist.id}), 201

@api.route('/playlists/<int:playlist_id>/songs', methods=['POST'])
def add_song_to_playlist(playlist_id):
    data = request.get_json()
    song_id = data.get('song_id')
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify({'message': 'Playlist not found'}), 404
    song = Song.query.get(song_id)
    if not song:
        return jsonify({'message': 'Song not found'}), 404
    playlist.songs.append(song)
    db.session.commit()
    return jsonify({'message': 'Song added to playlist successfully'}), 200