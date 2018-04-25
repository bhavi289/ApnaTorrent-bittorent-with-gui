import Manage_torrent_peers
import logging

class Run(object):
    
    def __init__(self):
        import Queue
        import Torrent_info

        queue_of_new_peers = Queue.Queue()
        import Torrent_trackers 
        import Manage_torrent_pieces
        import Seek_torrent_peers
        self.torrent_information = Torrent_info.torrent_info("1.torrent")
        self.torrent_tracker = Torrent_trackers.Torrent_trackers(self.torrent_information,queue_of_new_peers)

        self.seek_torrent_peer = Seek_torrent_peers.Seek_torrent_peers(queue_of_new_peers, self.torrent_information)
        self.manageTorrentPieces = Manage_torrent_pieces.Manage_torrent_pieces(self.torrent_information)
        self.manageTorrentPeers = Manage_torrent_peers.Manage_torrent_peers(self.torrent_information,self.manageTorrentPieces)

        self.manageTorrentPeers.start()
        self.seek_torrent_peer.start()
        self.manageTorrentPieces.start()

    def start(self):
        old=0

        while not self.manageTorrentPieces.arePiecesCompleted():
            if len(self.manageTorrentPeers.unchokedPeers) >= 1:
                for piece in self.manageTorrentPieces.pieces:
                    if not piece.finished:
                        pieceIndex = piece.pieceIndex
                        peer = self.manageTorrentPeers.getUnchokedPeer(pieceIndex)
                        if not peer:
                            continue
                        data = self.manageTorrentPieces.pieces[pieceIndex].getEmptyBlock()
                        if data:
                            index, offset, length = data
                            self.manageTorrentPeers.requestNewPiece(peer,index, offset, length)
                        piece.isComplete()
                        for block in piece.blocks:
                            import time
                            if ( int(time.time()) - block[3] ) > 8 and block[0] == "Pending" :
                                block[0] = "Free"
                                block[3] = 0
                b=0
                for i in range(self.manageTorrentPieces.numberOfPieces):
                    for j in range(self.manageTorrentPieces.pieces[i].num_blocks):
                        if self.manageTorrentPieces.pieces[i].blocks[j][0]=="Full":
                            b+=len(self.manageTorrentPieces.pieces[i].blocks[j][2])
                if b == old:
                    continue

                old = b
                print "Number of peers: ",len(self.manageTorrentPeers.unchokedPeers)," Completed: ",float((float(b) / self.torrent_information.totalLength)*100),"%"

            import time
            time.sleep(0.1)
