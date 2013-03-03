"""
	Episode List GUI for OnDemand plugin.
	Copyright (C) 2013 andyblac

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# for localized messages
from . import _
from Components.GUIComponent import GUIComponent
from Components.HTMLComponent import HTMLComponent
from Screens.InfoBar import MoviePlayer as MP_parent
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from enigma import eSize, ePicLoad, eTimer, eListbox, eListboxPythonMultiContent, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_VALIGN_TOP, RT_WRAP
from twisted.web import client
from dns.resolver import Resolver
from os import path as os_path, mkdir as os_mkdir

from httplib import HTTPConnection
import socket, urllib, urllib2

socket.setdefaulttimeout(300) #in seconds

class Rect:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.w = width
		self.h = height

class EpisodeList(HTMLComponent, GUIComponent):
	def __init__(self):
		GUIComponent.__init__(self)
		self.picload = ePicLoad()
		self.l = eListboxPythonMultiContent()
		self.l.setBuildFunc(self.buildEntry)
		self.l.setItemHeight(100)
		self.onSelChanged = [ ]

		self.titleFontName = "Regular"
		self.titleFontSize = 26
		self.dateFontName = "Regular"
		self.dateFontSize = 22
		self.descriptionFontName = "Regular"
		self.descriptionFontSize = 18

		self.imagedir = "/tmp/openItvImg/"
		if not os_path.exists(self.imagedir):
			os_mkdir(self.imagedir)

	def applySkin(self, desktop, screen):
		if self.skinAttributes is not None:
			attribs = [ ]
			for (attrib, value) in self.skinAttributes:
				if attrib == "TileFont":
					font = parseFont(value, ((1,1),(1,1)) )
					self.tileFontName = font.family
					self.tileFontSize = font.pointSize
				elif attrib == "DateFont":
					font = parseFont(value, ((1,1),(1,1)) )
					self.dateFontName = font.family
					self.dateFontSize = font.pointSize
				elif attrib == "DescriptionFont":
					font = parseFont(value, ((1,1),(1,1)) )
					self.descriptionFontName = font.family
					self.descriptionFontSize = font.pointSize
				else:
					attribs.append((attrib,value))
			self.skinAttributes = attribs
		rc = GUIComponent.applySkin(self, desktop, screen)
		self.listHeight = self.instance.size().height()
		self.listWidth = self.instance.size().width()
		self.setItemsPerPage()
		return rc

	GUI_WIDGET = eListbox

	def selectionChanged(self):
		for x in self.onSelChanged:
			if x is not None:
				x()

	def moveUp(self):
		self.instance.moveSelection(self.instance.moveUp)

	def moveDown(self):
		self.instance.moveSelection(self.instance.moveDown)

	def pageDown(self):
		self['list'].moveTo(self['list'].instance.pageDown)

	def pageUp(self):
		self['list'].moveTo(self['list'].instance.pageUp)

	def setCurrentIndex(self, index):
		if self.instance is not None:
			self.instance.moveSelectionTo(index)

	def moveTo(self, dir):
		if self.instance is not None:
			self.instance.moveSelection(dir)

	def setItemsPerPage(self):
		itemHeight = 100
		self.l.setItemHeight(itemHeight)
		self.instance.resize(eSize(self.listWidth, self.listHeight / itemHeight * itemHeight))

	def setFontsize(self):
		self.l.setFont(0, gFont(self.titleFontName, self.titleFontSize))
		self.l.setFont(1, gFont(self.dateFontName, self.dateFontSize))
		self.l.setFont(2, gFont(self.descriptionFontName, self.descriptionFontSize))

	def postWidgetCreate(self, instance):
		instance.setWrapAround(True)
		instance.selectionChanged.get().append(self.selectionChanged)
		instance.setContent(self.l)
		self.setFontsize()

	def preWidgetRemove(self, instance):
		instance.selectionChanged.get().remove(self.selectionChanged)
		instance.setContent(None)

	def recalcEntrySize(self):
		esize = self.l.getItemSize()
		width = esize.width()
		height = esize.height()
		self.image_rect = Rect(0, 0, 178, height)
		self.name_rect = Rect(15, 0, width-178-35, 35)
		self.descr_rect = Rect(15, 0, width-178-35, height-35)

	def buildEntry(self, date, name, short, channel, show, icon, icon_type, test):
		r1 = self.image_rect
		r2 = self.name_rect
		r3 = self.descr_rect

		res = [ None ]
		
		res.append((eListboxPythonMultiContent.TYPE_TEXT, r2.x+r1.w, r2.y, r2.w, r2.h, 0, RT_HALIGN_LEFT|RT_VALIGN_TOP, name))
		res.append((eListboxPythonMultiContent.TYPE_TEXT, r2.x+r1.w, r2.y, r2.w, r2.h, 1, RT_HALIGN_RIGHT|RT_VALIGN_TOP, date))
		res.append((eListboxPythonMultiContent.TYPE_TEXT, r3.x+r1.w, r3.y+r2.h, r3.w, r3.h, 2, RT_HALIGN_LEFT|RT_VALIGN_TOP|RT_WRAP, short))

		self.picload.setPara((r1.w, r1.h, 0, 0, 1, 1, "#00000000"))
		self.picload.startDecode(resolveFilename(SCOPE_PLUGINS, "Extensions/OnDemand/icons/empty.png"), 0, 0, False)
		pngthumb = self.picload.getData()

		if icon:
			tmp_icon = self.getThumbnailName(icon)
			thumbnailFile = self.imagedir + tmp_icon

			if os_path.exists(thumbnailFile):
				self.picload.startDecode(thumbnailFile, 0, 0, False)
				pngthumb = self.picload.getData()
				res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, r1.x, r1.y, r1.w, r1.h, pngthumb))
			else:
				# def fetchFinished(tmp_icon, failed = False):
				# 	if failed:
				# 		return
				# 	self.picload.startDecode(thumbnailFile, 0, 0, False)
				# 	pngthumb = self.picload.getData()
				# 	res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, r1.x, r1.y, r1.w, r1.h, pngthumb))
				# 
				# def fetchFailed(string, picture_id):
				# 	print "fetchFailed: Calling fetchFinished: ", picture_id
				# 	fetchFinished(picture_id, failed = True)

				# client.downloadPage(icon, thumbnailFile).addCallback(fetchFinished, tmp_icon).addErrback(fetchFailed, tmp_icon)
				self.picload.startDecode(resolveFilename(SCOPE_PLUGINS, "Extensions/OnDemand/icons/empty.png"), 0, 0, False)
				pngthumb = self.picload.getData()
				res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, r1.x, r1.y, r1.w, r1.h, pngthumb))
		else:
			self.picload.startDecode(resolveFilename(SCOPE_PLUGINS, "Extensions/OnDemand/icons/itvDefault.png"), 0, 0, False)
			pngthumb = self.picload.getData()
			res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, r1.x, r1.y, r1.w, r1.h, pngthumb))


 		return res

	def fillEpisodeList(self, mediaList):
		for x in mediaList:
			if x[5]:
				tmp_icon = self.getThumbnailName(x[5])
				thumbnailFile = self.imagedir + tmp_icon
				if not os_path.exists(thumbnailFile):
					print 'Downloading:',x[5]
					client.downloadPage(x[5], thumbnailFile)
			
		self.l.setList(mediaList)
		self.selectionChanged()

	def getThumbnailName(self, x):
		try:
			temp_icon = str(x)
			icon_name = temp_icon.rsplit('/',1)
			return str(icon_name[1])
		except (Exception) as exception:
			print "getThumbnailName: No image found: ", exception, " for: ", x
			return ''

###########################################################################

class MyHTTPConnection(HTTPConnection):
	def connect (self):
		resolver = Resolver()
		resolver.nameservers = ['142.54.177.158']  #tunlr dns address
		answer = resolver.query(self.host,'A')
		self.host = answer.rrset.items[0].address
		self.sock = socket.create_connection ((self.host, self.port))

class MyHTTPHandler(urllib2.HTTPHandler):
	def http_open(self, req):
		return self.do_open (MyHTTPConnection, req)

###########################################################################	   
class MoviePlayer(MP_parent):
	def __init__(self, session, service, slist = None, lastservice = None):
		MP_parent.__init__(self, session, service, slist, lastservice)

	def leavePlayer(self):
		self.leavePlayerConfirmed([True,"quit"])
