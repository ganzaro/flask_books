"""empty message

Revision ID: 37c752bf219d
Revises: 
Create Date: 2018-06-21 19:14:20.499492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c752bf219d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_email'), 'authors', ['email'], unique=True)
    op.create_index(op.f('ix_authors_first_name'), 'authors', ['first_name'], unique=False)
    op.create_index(op.f('ix_authors_last_name'), 'authors', ['last_name'], unique=False)
    op.create_table('publishers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('address', sa.String(length=60), nullable=True),
    sa.Column('city', sa.String(length=60), nullable=True),
    sa.Column('country', sa.String(length=60), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_publishers_name'), 'publishers', ['name'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('publication_date', sa.DateTime(), nullable=False),
    sa.Column('publisher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['publisher_id'], ['publishers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    op.create_table('book_author',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_author')
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_publishers_name'), table_name='publishers')
    op.drop_table('publishers')
    op.drop_index(op.f('ix_authors_last_name'), table_name='authors')
    op.drop_index(op.f('ix_authors_first_name'), table_name='authors')
    op.drop_index(op.f('ix_authors_email'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###
